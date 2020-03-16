#
# Index file
#
#

# Dependencies
import threading

# Local dependencies
from grid import Grid
from player import Player

# Function to move players
def move(player, grid, semaphore):
    # Initialise step counter
    counter = 0
    # Open file for writing
    file = open("./plMove/"+player.getId()+".txt", 'w')

    while True:
        # Acquire semaphore
        semaphore.acquire()
        print("here: ", player.getId())
        # Check if player should move
        if not player.getHungerStatus():
            if player.getSafetyStatus():
                # Release semaphore
                semaphore.release()
                break
        # Update player target
        player.nextTarget(grid.getGrid())
        # Move player towards target
        grid.movePlayer(player.getId(), player.getLocation(), player.getNextStep())
        file.write("---\n")
        # Call function to get snapshot
        snapshot = grid.getGrid()
        # Iterate over snapshot and print each element
        for row in snapshot:
            for elem in row:
                file.write(elem)
                file.write("\t")
            file.write("\n")
        # Update number of moves
        counter = counter+1
        if counter > 11:
            # Release semaphore
            semaphore.release()
            break
        else:
            # Release semaphore
            semaphore.release()
    file.close()


def init():
    # Set grid size
    gridSize = 10

    # Set no of players
    noOfPlayers = 3

    # Initialise players array
    players = []

    # Initialise grid object
    grid = Grid(gridSize)

    # Initialise threads
    threads = []

    # Initialise semaphore for grid
    semaphore = threading.Semaphore(1)

    for i in range(noOfPlayers):
        players.append(Player())

    # Place player on grid
    for player in players:
        # Place players on grid
        grid.playerStart(player)
        # Search for each player's next target
        player.nextTarget(grid.getGrid())
        # Initialise a thread for each player
        threads.append(threading.Thread(target=move, args=[player, grid, semaphore]))

    # Print grid
    grid.displayGrid()

    # Start all threads
    for thread in threads:
        thread.start()

init()
