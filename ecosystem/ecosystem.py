#
# File containing code for ecosystem
#
#

# Dependencies
import json
import random
import threading
import time
import os

# Local dependencies
from player import Player
from search import Search
from grid.grid import Grid
from ecosystem.getTarget import getTarget
from ecosystem.getNextStep import getNextStep
from ecosystem.getRandomCoordinates import getRandomCoordinates
from ecosystem.writeLogs import writeLogs

# Initialise class
class Ecosystem:
    # Initialise constructor
    def __init__(self):
        """Read config file and initialise default parameters."""
        # Open grid config file
        file = open("./gridConfig.json")
        # Read grid config from file
        gridConfig = json.load(file)
        # Close file
        file.close()

        # Initialise base path to logging directory
        self.baseLogDir = gridConfig["baseLogDir"]

        # Initialise path to log current events
        self.currentLogDir = None

        # Initilaise number of days
        self.noOfDays = gridConfig["noOfDays"]

        # Initialise grid size
        self.gridSize = gridConfig["gridSize"]

        # Initialise grid with grid size
        self.grid = Grid(self.gridSize)

        # Initialise a lock for grid
        self.gridLock = threading.Semaphore()

        # Initialise food limit
        self.foodLimit = gridConfig["foodLimit"]

        # Initialise array to hold players
        self.players = []

        # Initialise array to hold threads
        self.threads = []

        # Iterate till player limit is reached
        for i in range(gridConfig["noOfPlayers"]):
            # Call function to create players
            self.initialisePlayer()

    # Function to create players and place them on grid
    def initialisePlayer(self):
        """Create a new player object and place in along a grid edge."""
        # Initialise player
        player = Player()
        # Choose random coordinates
        coordinate = (random.randint(0, self.gridSize-1), random.randint(0, 1)*(self.gridSize-1))
        # Toss to check if coordinates should be reversed
        if random.randint(1,2) == 1:
            # Reverse coordinates
            coordinate = coordinate[::-1]
        # Update location for player
        player.updateLocation(coordinate)
        # Add player to players array
        self.players.append(player)
        # Acquire lock
        self.gridLock.acquire()
        # Add player to coordinate
        self.grid.grid[coordinate[0]][coordinate[1]].addPlayer(player)
        # Release lock
        self.gridLock.release()
        # Return player
        return player

    # Function to get player target
    def getTargetLocation(self, currentLocation, target, visionLimit):
        """Get snapshot of grid and call search function to locate target.

        Keyword arguments:
        currentLocation -- tuple
        target -- string in 'food' or 'home'
        visionLimit -- integer
        """
        # Initialise target
        targetLocation = None
        # Check if target is among valid targets
        if target in ["food", "home"]:
            # Acquire lock
            self.gridLock.acquire()
            # Get snapshot of grid
            snapshot = self.grid.getSnapshot(target)
            # Release lock
            self.gridLock.release()
            # Check if target is food
            if target == "food":
                # Initialise search
                search = Search(snapshot, currentLocation, "F", visionLimit)
            elif target == "home":
                # Initialise search
                search = Search(snapshot, currentLocation, "H", visionLimit)
            # Get target location
            targetLocation = search.locateTarget()
        # TODO: throw error (invalid target)
        # else:
        return targetLocation

    # Function to print snapshot of grid
    def displayGrid(self, target="all"):
        """Get snapshot of grid and print it element wise.

        Keyword arguments:
        target -- string in 'all', 'food' or 'home'
        """
        # Check if target is among valid targets
        if target in ["all", "food", "home"]:
            # Acquire lock
            self.gridLock.acquire()
            # Get snapshot of grid
            snapshot = self.grid.getSnapshot(target)
            # Release lock
            self.gridLock.release()
            # Print a divider
            print("---###---")
            # Iterate over each row
            for i in range(self.gridSize):
                # Iterate over each column
                for j in range(self.gridSize):
                    # Print cell
                    print(snapshot[i][j], end="\t")
                # Enter new line for each row
                print()
        # TODO: throw error (invalid target)
        # else:

    # Function to write snapshot of grid to log file
    def logGrid(self):
        """Get snapshot of grid and write it to log file."""
        # Acquire lock
        self.gridLock.acquire()
        # Get snapshot of grid
        snapshot = self.grid.getSnapshot("all")
        # Release lock
        self.gridLock.release()
        # Iterate over each row
        for i in range(self.gridSize):
            # Iterate over each column
            for j in range(self.gridSize):
                # Print cell
                writeLogs(self.currentLogDir, "grid", str(snapshot[i][j])+",")
            # Enter new line for each row
            writeLogs(self.currentLogDir, "grid", "\n")

    # Function to calculate player's next move
    def calculateNextMove(self, currentLocation, hungerStatus, safetyStatus, visionLimit):
        """Calculate player's target and its current location. Return step to move towards target.

        Keyword arguments:
        currentLocation -- tuple
        hungerStatus -- boolean
        safetyStatus -- boolean
        visionLimit -- integer
        """
        # Initialise new location
        newLocation = currentLocation
        # Initialise target location
        targetLocation = None
        # Check parameter types
        if type(currentLocation) == type((1,2)) and type(hungerStatus) == type(True) and type(safetyStatus) == type(True):
            # Get player target
            target = getTarget(hungerStatus, safetyStatus)
            # Check if player target is not None
            if not target == None:
                # Get player target location
                targetLocation = self.getTargetLocation(currentLocation, target, visionLimit)
                # Check if target location is None
                if targetLocation == None:
                    # Call function to get randon coordinates
                    targetLocation = getRandomCoordinates(self.gridSize)
                # Get new location
                newLocation = getNextStep(currentLocation, targetLocation)
        # Return new location
        return targetLocation, newLocation

    # Function to move players
    def movePlayer(self, player):
        """Move player towards target.

        Keyword arguments:
        player -- player object
        """
        # Get player id
        playerId = player.getId()
        # Set movement limit
        maxMoves = player.getMovementLimit()
        # Iterate till movement limit is reached
        for move in range(maxMoves):
            # Get player current location
            currentLocation = player.getLocation()
            # Call function to get new location to move to
            targetLocation, newLocation = self.calculateNextMove(currentLocation, player.getHungerStatus(), player.getSafetyStatus(), player.getVisionLimit())
            # Prepare string to write to log file
            logString = str(player.getHungerStatus())
            logString = logString +","+str(player.getSafetyStatus())
            logString = logString +","+str(currentLocation[0])+","+str(currentLocation[1])
            logString = logString +","+str(targetLocation[0])+","+str(targetLocation[1])
            logString = logString +","+str(newLocation[0])+","+str(newLocation[1])+"\n"
            # Write player state to file
            writeLogs(self.currentLogDir, playerId, logString)
            # Check if new location matches current location
            if not newLocation == currentLocation:
                # Acquire lock
                self.gridLock.acquire()
                # Move player
                self.grid.movePlayer(playerId, currentLocation, newLocation)
                # Update player safety status
                player.updateSafetyStatus(self.grid.grid[newLocation[0]][newLocation[1]].isSafe())
                # Check if player has reached target
                if newLocation == targetLocation:
                    # Check if player is hungry and cell has food
                    if player.getHungerStatus() and self.grid.grid[newLocation[0]][newLocation[1]].foodExists():
                        # Remove food from cell
                        self.grid.grid[newLocation[0]][newLocation[1]].modifyFoodCount("decrement")
                        # Update player's hunger status
                        player.updateHungerStatus(False)
                # Release lock
                self.gridLock.release()
            # Check if hunger is False and safety is True
            if not player.getHungerStatus() and player.getSafetyStatus():
                # Break from loop
                break
            # Wait till recharge duration ends
            time.sleep(player.getRechargeDuration())

    # Function to assign thread to each player
    def assignThreads(self):
        """Iterate over players and assign a thread to each."""
        # Iterate over each player
        for player in self.players:
            # Create a thread and append to array
            self.threads.append(threading.Thread(target=self.movePlayer, args=[player]))

    # Function to perfrom day activities
    def beginDay(self):
        """Call functions to initialise food, assign threads and start threads."""
        # Acquire lock
        self.gridLock.acquire()
        # Initialise food on grid
        self.grid.initialiseFood(self.foodLimit)
        # Release lock
        self.gridLock.release()
        # Log grid state to file
        self.logGrid()
        # Call function to assign threads to players
        self.assignThreads()
        # Iterate over all threads
        for thread in self.threads:
            # Start thread
            thread.start()
        # Sleep tillall threads complete execution
        while threading.active_count() > 1:
            time.sleep(1)

    # Function to perform night activities
    def beginNight(self):
        """Call function to reset food on grid and remove players who do not meet end conditions."""
        # Acquire lock
        self.gridLock.acquire()
        # Call function to reset food on grid
        self.grid.resetFood()
        # Release lock
        self.gridLock.release()
        # Iterate over all players
        for player in self.players:
            # Call function to update player parameters
            player.updateParameters()
            # Initialise string with player movemment limit, vision limit and recharge duration
            logString = str(player.getId())
            logString = logString+","+str(player.getMovementLimit())
            logString = logString+","+str(player.getVisionLimit())
            logString = logString+","+str(player.getRechargeDuration())+"\n"
            # Write log to file
            writeLogs(self.currentLogDir, "playerConfig", logString)
            # Check if player is hungry or is in unsafe cell
            if player.getHungerStatus() or not player.getSafetyStatus():
                # Get player location
                location = player.getLocation()
                # Acquire lock
                self.gridLock.acquire()
                # Remove player from grid
                self.grid.grid[location[0]][location[1]].removePlayer(player.getId())
                # Release lock
                self.gridLock.release()
        # Remove hungry players
        self.players = [player for player in self.players if not player.getHungerStatus()]
        # Remove players in unsafe cells
        self.players = [player for player in self.players if player.getSafetyStatus()]
        # Reset threads
        self.threads = []
        # Iterate over all players
        for player in self.players:
            # Check if player should reproduce
            if random.uniform(0,1) < player.getReproductionChance():
                # Reset player reproduction chance
                player.updateReproductionChance("reset")
                # Get player config
                config = player.getConfig()
                # Create a new player object
                newPlayer = self.initialisePlayer()
                # Update new player config
                newPlayer.updateConfig(config)
            else:
                # Increment reproduction chances
                player.updateReproductionChance("increment")
            # Set player hunger status to True
            player.updateHungerStatus(True)


    # Function to start simulation
    def startSimulation(self):
        """Initialise log directory and call functions to start and complete cycle."""
        # Iterate over number of days
        for i in range(self.noOfDays):
            # Set current log dir
            self.currentLogDir = os.path.join(self.baseLogDir, "day"+str(i))
            # Create a directory for logging
            os.makedirs(self.currentLogDir)
            # Acquire lock
            self.gridLock.acquire()
            # Update log directory path in grid
            self.grid.updateLogDirectoryLocation(self.currentLogDir)
            # Release lock
            self.gridLock.release()
            # Call function to begin day
            self.beginDay()
            # Call function to begin night
            self.beginNight()
            # If player array is empty, exit loop
            if not len(self.players) > 0:
                # Exit loop
                break
