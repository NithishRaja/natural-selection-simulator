#
# Index file
#
#

# Dependencies
import threading, time

# Local dependencies
from grid import Grid
from player import Player

# Function to move players
def move(player, grid, semaphore):
    # Initialise step counter
    counter = 0
    # Open file for writing
    file = open("./plMove/"+player.getId()+".txt", 'a')

    while True:
        # Acquire semaphore
        semaphore.acquire()
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

    for i in range(noOfPlayers):
        players.append(Player())

    # Initialise grid object
    grid = Grid(gridSize)

    for i in range(2):
        # Call function to reset grid
        grid.fillZeros(False)
        # Call function to fill grid with food
        grid.initialiseFood()

        # Initialise threads
        threads = []

        # Initialise semaphore for grid
        semaphore = threading.Semaphore(1)

        # Place player on grid
        for player in players:
            # Place players on grid in current iteration is the initial iteration
            if i == 0:
                # Place players on grid
                grid.playerStart(player)
            else:
                # Update hunger status if current iretation is not initial interation
                player.setHungerStatus(True)
            # Search for each player's next target
            player.nextTarget(grid.getGrid())
            # Initialise a thread for each player
            threads.append(threading.Thread(target=move, args=[player, grid, semaphore]))

        print("---")

        # Print grid
        grid.displayGrid()

        # Start all threads
        for thread in threads:
            thread.start()

        time.sleep(5)
init()
