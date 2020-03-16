#
# Index file
#
#

# Dependencies
import threading
import time
import os

# Local dependencies
from grid import Grid
from player import Player

# Function to move players
def move(day, player, grid, semaphore):
    # Initialise step counter
    counter = 0
    # Open file for writing
    file = open("./logging/day"+str(day)+"/"+player.getId()+".txt", 'w')

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
        # Get player info
        playerLocation = player.getLocation()
        playerNextStep = player.getNextStep()
        playerTarget = player.getTarget()
        # Move player towards target
        grid.movePlayer(player.getId(), playerLocation, playerNextStep)
        # Build string to write to file
        string = "("+str(playerLocation[0])+", "+str(playerLocation[1])+"),"
        string = string + "("+str(playerTarget[0])+", "+str(playerTarget[1])+"),"
        string = string + "("+str(playerNextStep[0])+", "+str(playerNextStep[1])+")\n"
        # Write log to file
        file.write(string)
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
        # Initialise logging directory
        logDir = os.path.join("logging", "day"+str(i))
        # CHeck if directory for current day logging exists
        if not os.path.exists(logDir):
            # Create directory for logging
            os.makedirs(logDir)
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
            threads.append(threading.Thread(target=move, args=[i, player, grid, semaphore]))

        # Open file
        file = open(os.path.join(logDir, "grid.txt"), "w")
        # Call function to get snapshot
        snapshot = grid.getGrid()
        # Iterate over snapshot and print each element
        for row in snapshot:
            for elem in row:
                file.write(elem)
                file.write("\t")
            file.write("\n")

        # Start all threads
        for thread in threads:
            thread.start()

        time.sleep(5)
init()
