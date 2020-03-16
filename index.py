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
def move(player, grid):
    # Initialise lock for grid
    lock = threading.RLock()
    # Initialise step counter
    counter = 0
    # Open file for writing
    file = open("./plMove/"+player.getId()+".txt", 'w')

    while True:
        # Acquire lock
        lock.acquire()
        # Check if player should move
        if not player.getHungerStatus():
            if player.getSafetyStatus():
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
            break
        # Release lock
        lock.release()
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

    for i in range(noOfPlayers):
        players.append(Player())

    # Place player on grid
    for player in players:
        # Place players on grid
        grid.playerStart(player)
        # Search for each player's next target
        player.nextTarget(grid.getGrid())
        # Initialise a thread for each player
        threads.append(threading.Thread(target=move, args=[player, grid]))

    # Print grid
    grid.displayGrid()

    # Start all threads
    for thread in threads:
        thread.start()

init()
