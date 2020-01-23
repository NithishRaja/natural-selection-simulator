#
# File containing class for Grid
#
#

# Initialise class
class Grid:
    # Get all grid configurations
    def __init__(self, gridSize=10):
        """Get grid size and create an empty grid"""
        # Initialise grid size
        self.gridSize = gridSize

        # initialise grid
        self.grid = []

        # Call function to fill grid with zeroes
        self.fillZero()

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

    # Function to display grid
    def displayGrid(self):
        # Iterate over each row in grid
        for row in self.grid:
            # Iterate over each element in row
            for elem in row:
                # Print element without '\n'
                print(elem, end="")
            # Move cursor to next line
            print()
