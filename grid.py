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
        """Get grid size and create an empty grid

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
        self.fillZero()

        # Call function to fill grid with food
        self.initialiseFood()

    # Function to fill grid with zeroes
    def fillZero(self):
        """Set grid to empty array and fill with zeroes"""
        # Set grid to empty array
        self.grid = []
        # Iterate over each grid element
        for i in range(self.gridSize):
            # Initialise a new row in grid
            self.grid.append([])
            for j in range(self.gridSize):
                # Fill row with zeroes
                self.grid[i].append(0)

    # Function to randomly set food in cells
    def initialiseFood(self):
        """Select a cell randomly and if empty, place food in it"""
        # Add food to grid till food limit is reached
        while self.foodCounter<self.foodLimit:
            # Get a random position
            x = randint(1, self.gridSize-2)
            y = randint(1, self.gridSize-2)
            # Check if cell is empty
            if self.grid[x][y] == 0:
                # Place food in empty cell
                self.grid[x][y] = 'F'
                # Update food count
                self.foodCounter = self.foodCounter + 1

    # Function to return grid
    def getGrid(self):
        """Return the grid"""
        return self.grid

    # Function to display grid
    def displayGrid(self):
        """Iterate over grid and print it as a matrix"""
        # Iterate over each row in grid
        for row in self.grid:
            # Iterate over each element in row
            for elem in row:
                # Print element without '\n'
                print(elem, end="")
            # Move cursor to next line
            print()

grid = Grid()
grid.displayGrid()
