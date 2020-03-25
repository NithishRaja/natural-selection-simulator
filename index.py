#
# Test file
#
#

# Dependencies
import json
import random

# Local dependencies
from player import Player
from search import Search
from grid.grid import Grid

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

        # Initialise grid size
        self.gridSize = gridConfig["gridSize"]

        # initialise grid with grid size
        self.grid = Grid(self.gridSize)

        # Initialise food on grid
        self.grid.initialiseFood(gridConfig["foodLimit"])

        # Initialise array to hold players
        self.players = []

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
        # Toss to reverse coordinates
        toss = random.randint(1,2)
        # Check if coordinates should be reversed
        if toss == 1:
            # Reverse coordinates
            coordinate = coordinate[::-1]
        # Update location for player
        player.updateLocation(coordinate)
        # Add player to players array
        self.players.append(player)
        # Add player to coordinate
        self.grid.grid[coordinate[0]][coordinate[1]].addPlayer(player)

    # Function to get player target
    def getTarget(self, hungerStatus, safetyStatus):
        """Get player target based on player status.

        Keyword arguments:
        hungerStatus -- boolean
        safetyStatus -- boolean
        """
        # Initialise target
        target = None
        # Check if hungerStatus and safetyStatus are boolean
        if type(hungerStatus) == type(True) and type(safetyStatus) == type(True):
            # Check hunger status of player
            if hungerStatus:
                # Set player target to food
                target = "food"
            # Check safety status of player
            elif not safetyStatus:
                # Set player target to home
                target = "home"
        # Return target
        return target

    # Function to get player target
    def getTargetLocation(self, currentLocation, target):
        """Get snapshot of grid and call search function to locate target.

        Keyword arguments:
        currentLocation -- tuple
        target -- string in 'food' or 'home'
        """
        # Initialise target
        targetLocation = None
        # Check if target is among valid targets
        if target in ["food", "home"]:
            # Get snapshot of grid
            snapshot = self.grid.getSnapshot(target)
            # Check if target is food
            if target == "food":
                # Initialise search
                search = Search(snapshot, currentLocation, "F", None)
            elif target == "home":
                # Initialise search
                search = Search(snapshot, currentLocation, "H", None)
            # Get target location
            targetLocation = search.locateTarget()
        # TODO: throw error (invalid target)
        # else:
        return targetLocation

    # Function to calculate player's next step to reach target
    def getNextStep(self, currentLocation, targetLocation):
        """Calculate next step to reach target.

        Keyword arguments:
        currentLocation -- tuple
        targetLocation -- tuple
        """
        # Initialise tuple for new location
        newLocation = [coordinate for coordinate in currentLocation]
        # check if parameters passed are tuples
        if type(currentLocation) == type((1,2)) and type(targetLocation) == type((1,2)):
            # Check if x coordinate needs to be incremented
            if currentLocation[0] < targetLocation[0]:
                newLocation[0] = currentLocation[0]+1
            # Check if x coordinate needs to be decremented
            elif currentLocation[0] > targetLocation[0]:
                newLocation[0] = currentLocation[0]-1
            # Check if y coordinate needs to be incremented
            if currentLocation[1] < targetLocation[1]:
                newLocation[1] = currentLocation[1]+1
            # Check if x coordinate needs to be decremented
            elif currentLocation[1] > targetLocation[1]:
                newLocation[1] = currentLocation[1]-1
        # TODO: throw error (parameters must of type tuple)
        # else:
        # Convert new location to tuple
        newLocation = tuple(newLocation)
        # Return new location
        return newLocation

    # Function to print snapshot of grid
    def displayGrid(self, target="all"):
        """Get snapshot of grid and print it element wise.

        Keyword arguments:
        target -- string in 'all', 'food' or 'home'
        """
        # Check if target is among valid targets
        if target in ["all", "food", "home"]:
            # Get snapshot of grid
            snapshot = self.grid.getSnapshot(target)
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

    # Function to get random coordinates
    def getRandomCoordinates(self):
        """Generate random coordinates within grid."""
        # Generate random coordinates
        coordinates = (random.randint(0, self.gridSize-1), random.randint(0, self.gridSize-1))
        # Return coordinates
        return coordinates

    # Function to calculate player's next move
    def calculateNextMove(self, currentLocation, hungerStatus, safetyStatus):
        """Calculate player's target and its current location. Return step to move towards target.

        Keyword arguments:
        currentLocation -- tuple
        hungerStatus -- boolean
        safetyStatus -- boolean
        """
        # Initialise new location
        newLocation = currentLocation
        # Initialise target location
        targetLocation = None
        # Check parameter types
        if type(currentLocation) == type((1,2)) and type(hungerStatus) == type(True) and type(safetyStatus) == type(True):
            # Get player target
            target = self.getTarget(hungerStatus, safetyStatus)
            # Check if player target is not None
            if not target == None:
                # Get player target location
                targetLocation = self.getTargetLocation(currentLocation, target)
                # Check if target location is None
                if targetLocation == None:
                    # Call function to get randon coordinates
                    targetLocation = self.getRandomCoordinates()
                # Get new location
                newLocation = self.getNextStep(currentLocation, targetLocation)
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
        maxMoves = 10
        # Iterate till movement limit is reached
        for move in range(maxMoves):
            # display grid
            self.displayGrid()
            # Get player current location
            currentLocation = player.getLocation()
            # Call function to get new location to move to
            targetLocation, newLocation = self.calculateNextMove(currentLocation, player.getHungerStatus(), player.getSafetyStatus())
            # Check if new location matches current location
            if not newLocation == currentLocation:
                # Move player
                self.grid.movePlayer(playerId, currentLocation, newLocation)
                # Check if cell is safe
                if self.grid.grid[newLocation[0]][newLocation[1]].isSafe():
                    # Update player safety status
                    player.updateSafetyStatus(True)
                else:
                    # Update player safety status
                    player.updateSafetyStatus(False)
                # Check if player has reached target
                if newLocation == targetLocation:
                    # Check if player is hungry and cell has food
                    if player.getHungerStatus() and self.grid.grid[newLocation[0]][newLocation[1]].foodExists():
                        # Remove food from cell
                        self.grid.grid[newLocation[0]][newLocation[1]].modifyFoodCount("decrement")
                        # Update player's hunger status
                        player.updateHungerStatus(False)
            # Check if hunger is False and safety is True
            if not player.getHungerStatus() and player.getSafetyStatus():
                # Break from loop
                break

# Initialise ecosystem object
eco = Ecosystem()
# Iterate over all players
for player in eco.players:
    eco.movePlayer(player)
