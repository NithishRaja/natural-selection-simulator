#
# File containing class for Grid
#
#

# Dependencies
from random import randint

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
            if self.grid[x][y] == '0':
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
                else:
                    # If element in current cell is not a string, it is a player object
                    snapshot[i].append('P')
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
                print(elem, end="")
            print()

    # Function to place new player along edges
    def playerStart(self, player):
        """Place a player along the edgesself.

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
            # Check if position is empty
            if snapshot[coords[0]][coords[1]] == 'H':
                # Set location for player
                player.setLocation(coords)
                # Update grid
                self.grid[coords[0]][coords[1]] = player
                # Exit loop
                break
