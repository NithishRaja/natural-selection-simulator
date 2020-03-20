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
