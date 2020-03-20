#
# File containing code for grid
#
#

# Dependencies
import random

# Local dependencies
from grid.cell import Cell

# Initialise class
class Grid:
    # Initialise constructor
    def __init__(self, gridSize=10):
        """Set grid parameters to default values."""
        # Initialise grid size
        self.gridSize = gridSize

        # Initialise grid as empty array
        self.grid = []

        # Call function to initialise cells
        self.initialiseGrid()

        # Call function to mark safe edges
        self.markEdgesAsSafe()

    # Function to fill grid with cells
    def initialiseGrid(self):
        """Iterate over grid and initialise each cell."""
        # Iterate over rows in grid
        for i in range(self.gridSize):
            # Append array for each row
            self.grid.append([])
            # Iterate over columns in grid
            for j in range(self.gridSize):
                # Initialise cell
                self.grid[i].append(Cell())

    # Function to mark edges as safe cells
    def markEdgesAsSafe(self):
        """Iterate over all cells in grid and mark cells in edges as safe."""
        # Iterate over all rows
        for i in range(self.gridSize):
            # Iterate over all columns
            for j in range(self.gridSize):
                # Check if cell is along an edge
                if i == 0 or j == 0 or i == self.gridSize-1 or j == self.gridSize-1:
                    # Update cell safety to True
                    self.grid[i][j].updateSafety(True)

    # Function to add food on grid
    def initialiseFood(self, foodLimit=5):
        """Randomly select cells and increment their food values.

        Keyword arguments:
        foodLimit -- Integer indicating number of food to add to grid
        """
        # Iterate till food limit is reached
        for i in range(foodLimit):
            # Generate a random cell coordinate
            coordinate = (random.randint(1, self.gridSize-2), random.randint(1, self.gridSize-2))
            # Increment food in coordinate
            self.grid[coordinate[0]][coordinate[1]].modifyFoodCount("increment")
