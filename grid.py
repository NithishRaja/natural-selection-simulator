#
# File containing class for Grid
#
#

# Dependencies
from random import randint

# Local dependencies
from player import Player

# Initialise class
class Grid:
    # Get all grid configurations
    def __init__(self, gridSize=10, foodLimit=5):
        """Get grid size and create an empty grid.

        Keyword arguments:
        gridSize -- Integer mentioning the grid size (defaults to 10)
        foodLimit -- Integer to set maximum number of cells with food (defaults to 5)
        """
        # Initialise grid size
        self.gridSize = gridSize

        # initialise grid
        self.grid = []

        # Initialise food limit
        self.foodLimit = foodLimit

        # initialise food counter
        self.foodCounter = 0

        # Call function to fill grid with zeroes
        self.fillZeros(True)

        # Call function to fill grid with food
        self.initialiseFood()

    # Function to fill grid with zeroes
    def fillZeros(self, initial=False):
        """Iterate over grid and remove all food cells.
        Initialise grid with empty cells if initial flag is set to True.

        Keyword arguments:
        initial -- Flag to perform initialisation or not
        """
        # Check if initial flag is set to True
        if initial:
            # Set grid to empty array
            self.grid = []
            # Iterate over each grid element
            for i in range(self.gridSize):
                # Initialise a new row in grid
                self.grid.append([])
                for j in range(self.gridSize):
                    # Check if current position is along the edges
                    if i == 0 or j == 0:
                        # Add marker for edges
                        self.grid[i].append('H')
                    elif i == self.gridSize-1 or j == self.gridSize-1:
                        # Add marker for edges
                        self.grid[i].append('H')
                    else:
                        # Fill cell with zeros
                        self.grid[i].append('0')
        else:
            # Iterate over grid
            for i in range(1, self.gridSize-1):
                for j in range(1, self.gridSize-1):
                    # Check if cell has food
                    if type(self.grid[i][j]) == type("str") and self.grid[i][j] == 'F':
                        # Empty cell
                        self.grid[i][j] = '0'

    # Function to randomly set food in cells
    def initialiseFood(self):
        """Select a cell randomly and if empty, place food in it."""
        # Add food to grid till food limit is reached
        while self.foodCounter<self.foodLimit:
            # Get a random position
            x = randint(1, self.gridSize-2)
            y = randint(1, self.gridSize-2)
            # Check if cell is empty
            if type(self.grid[x][y]) == type('str') and self.grid[x][y] == '0':
                # Place food in empty cell
                self.grid[x][y] = 'F'
                # Update food count
                self.foodCounter = self.foodCounter + 1

    # Function to return grid
    def getGrid(self):
        """Return a snapshot of the actual grid."""
        # initialise variable to hold snapshot of grid
        snapshot = []
        # Iterate over grid
        for i in range(self.gridSize):
            snapshot.append([])
            # Iterate over each element in row
            for j in range(self.gridSize):
                # Check if element in current cell is a string
                if type(self.grid[i][j]) == type("a"):
                    # Update snapshot with element in current cell
                    snapshot[i].append(self.grid[i][j])
                # Check if current cell contains players
                elif type(self.grid[i][j]) == type([]):
                    # If element in current cell is not a string, it is a player object
                    snapshot[i].append('P'+str(len(self.grid[i][j])))
        # Return snapshot
        return snapshot

    # Function to display grid
    def displayGrid(self):
        """Get a snapshot of grid and print it."""
        # Call function to get snapshot
        snapshot = self.getGrid()
        # Iterate over snapshot and print each element
        for row in snapshot:
            for elem in row:
                print(elem, end="\t")
            print()

    # Function to place new player along edges
    def playerStart(self, player):
        """Place a player along the edges.

        Keyword arguments:
        player -- player object
        """
        # Get snapshot of grid
        snapshot = self.getGrid()
        # Initialise variable to hold start position
        coords = None
        # Get a starting position for player
        while True:
            if randint(1,100)%2==0:
                coords = (randint(0, self.gridSize-1), randint(0, 1)*(self.gridSize-1))
            else:
                coords = (randint(0, 1)*(self.gridSize-1), randint(0, self.gridSize-1))
            # Set location for player
            player.setLocation(coords)
            # Check if position is empty
            if snapshot[coords[0]][coords[1]] == 'H':
                # Update grid
                self.grid[coords[0]][coords[1]] = [player]
                # Exit loop
                break
            else:
                # Update grid
                self.grid[coords[0]][coords[1]].append(player)
                # Exit loop
                break

    # Function to move player
    def movePlayer(self, id, currentLocation, newLocation):
        """Move player from one cell to another and update player location.

        Keyword arguments:
        id -- string with player id
        currentLocation -- tuple with current location of player
        newLocation -- tuple with location to move player to
        """
        # Check if any player exists in current location
        if type(self.grid[currentLocation[0]][currentLocation[1]]) == type([]):
            # Initialise variable to hold player index
            playerIndex = -1
            # Iterate over all players
            for index, player in enumerate(self.grid[currentLocation[0]][currentLocation[1]]):
                # Check if player id matches
                if id == player.getId():
                    # Set player index
                    playerIndex = index
                    # Exit loop
                    break
            # Check if valid player index is set
            if playerIndex > -1:
                # Remove player from current list
                player = self.grid[currentLocation[0]][currentLocation[1]].pop(playerIndex)
                # Update player location
                player.setLocation(newLocation)
                # Check new location safety
                if newLocation[0] == 0 or newLocation[0] == self.gridSize-1:
                    # Update player safety status
                    player.setSafetyStatus(True)
                elif newLocation[1] == 0 or newLocation[1] == self.gridSize-1:
                    # Update player safety status
                    player.setSafetyStatus(True)
                else:
                    # Update player safety status
                    player.setSafetyStatus(False)
                # Check if new position has existing players
                if type(self.grid[newLocation[0]][newLocation[1]]) == type([]):
                    # Append player to list
                    self.grid[newLocation[0]][newLocation[1]].append(player)
                # New location does not have existing players
                elif type(self.grid[newLocation[0]][newLocation[1]]) == type(''):
                    # Check if new location has food
                    if self.grid[newLocation[0]][newLocation[1]] == 'F':
                        # Update player hungry status
                        player.setHungerStatus(False)
                    # Move player to new location
                    self.grid[newLocation[0]][newLocation[1]] = [player]
                # Check if other players exist in current location
                if len(self.grid[currentLocation[0]][currentLocation[1]]) == 0:
                    # Check current location safety
                    if currentLocation[0] == 0 or currentLocation[0] == self.gridSize-1:
                        # Update cell to home
                        self.grid[currentLocation[0]][currentLocation[1]] = 'H'
                    elif currentLocation[1] == 0 or currentLocation[1] == self.gridSize-1:
                        # Update cell to home
                        self.grid[currentLocation[0]][currentLocation[1]] = 'H'
                    else:
                        # Update cell to empty cell
                        self.grid[currentLocation[0]][currentLocation[1]] = '0'
            #else:
                # No player with given id found
                # TODO: throw error
