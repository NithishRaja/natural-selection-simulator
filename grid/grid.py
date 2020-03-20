#
# File containing code for grid
#
#

# Dependencies
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

        # Fill grid with cells
        # Iterate over rows in grid
        for i in range(self.gridSize):
            # Append array for each row
            self.grid.append([])
            # Iterate over columns in grid
            for j in range(self.gridSize):
                # Initialise cell
                self.grid[i].append(Cell())
