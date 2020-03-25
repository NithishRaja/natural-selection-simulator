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

    # Function to reset food on grid
    def resetFood(self):
        """Iterate over all cells and call function to reset food count to 0."""
        # Iterate over all rows
        for i in range(self.gridSize):
            # Iterate over all columns
            for j in range(self.gridSize):
                # Call function to reset food count
                self.grid[i][j].modifyFoodCount("reset")

    # Function to get snapshot of image
    def getSnapshot(self, target="all"):
        """Return a matrix representing the current state of the grid.

        Keyword arguments:
        target -- string representing the target to focus on
        """
        # Check if target is valid
        if target in ["all", "food", "home"]:
            # Initialise empty array for snapshot
            snapshot = []
            # Iterate over rows
            for i in range(self.gridSize):
                # Add row to snapshot
                snapshot.append([])
                # Iterate over columns
                for j in range(self.gridSize):
                    # Add empty cell to snapshot
                    snapshot[i].append("0")
                    # Check if target is food
                    if target == "food" and self.grid[i][j].foodExists():
                        # Modify cell to show food
                        snapshot[i][j] = "F"
                    # Check if target is home
                    if target == "home" and self.grid[i][j].isSafe():
                        # modify cell to show safe cells
                        snapshot[i][j] = "H"
                    if target == "all":
                        # modify cell to show status of cell
                        status = ""
                        # Check if cell is safe
                        if self.grid[i][j].isSafe():
                            status = status + "H"
                        else:
                            status = status + "0"
                        # Check if cell has food
                        if self.grid[i][j].foodExists():
                            status = status + "F"
                        # Update status with player count
                        status = status + "P" + str(self.grid[i][j].getPopulation())
                        # Add status to snapshot
                        snapshot[i][j] = status
            # Return snapshot
            return snapshot
        # TODO: return a error (invalid target)
        # else:

    # Function to move player from one cell to another
    def movePlayer(self, playerId, currentLocation, newLocation):
        """Remove player from players array in one cell and append it to another cell.

        Keyword arguments:
        playerId -- string
        currentLocation -- tuple
        newLocation -- tuple
        """
        # Check if current location and new location are tuples
        if type(currentLocation) == type((1,2)) and type(newLocation) == type((1,2)):
            # Call remove player function on current cell
            response = self.grid[currentLocation[0]][currentLocation[1]].removePlayer(playerId)
            # Check if response is a boolean
            if not type(response) == type(True):
                # Update player location
                response.updateLocation(newLocation)
                # Add player to new location
                self.grid[newLocation[0]][newLocation[1]].addPlayer(response)
        # TODO: throw error (parameter type mismatch)
        # else:
