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
    def getTarget(self, player):
        """Get player target based on player status.

        Keyword arguments:
        playerIndex -- player object
        """
        # Initialise target
        target = None
        # Check hunger status of player
        if player.getHungerStatus():
            # Set player target to food
            target = "food"
        # Check safety status of player
        elif not player.getSafetyStatus():
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
            # Initialise search
            search = Search(snapshot, currentLocation, "F", None)
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

    # Function to move players
    def movePlayer(self, player):
        # Get player id
        playerId = player.getId()
        # Set movement limit
        maxMoves = 10
        # Iterate till movement limit is rached
        for move in range(maxMoves):
            # display grid
            eco.displayGrid()
            print("---")
            # Get player target
            target = eco.getTarget(player)
            # Check if player target is not None
            if not target == None:
                # Get current location
                currentLocation = player.getLocation()
                # Get player target location
                targetLocation = eco.getTargetLocation(currentLocation, target)
                # TODO: if target location is None, get a random target location
                # Get new location
                newLocation = eco.getNextStep(currentLocation, targetLocation)
                # Check if new location matches current location
                if not newLocation == currentLocation:
                    # Move player
                    eco.grid.movePlayer(playerId, currentLocation, newLocation)
                    # Check if player has reached target
                    # TODO: If player has reached target, update player hunger and safety

# Initialise ecosystem object
eco = Ecosystem()
# Iterate over all players
for player in eco.players:
    eco.movePlayer(player)
