#
# File containing code for searching grid
#
#

# Dependencies

# Initialise class
class Search:
    # Initialise constructor
    def __init__(self, grid, location, target, radius):
        """Initialise parameters and calculate grid size.

        Keyword arguments:
        grid -- matrix representing state of grid
        location -- tuple with starting locaation for search
        target -- string representing target
        radius -- integer representing radius to limit search to
        """
        # Initialise grid
        self.grid = grid

        # Initialise location
        self.location = location

        # Initialise target
        self.target = target

        # Initialise radius
        self.radius = radius

        # Calculate grid size
        self.gridSize = len(self.grid)

        # Initialise lower limit
        self.lowerLimit = [0, 0]

        # Initialise upper limit
        self.upperLimit = [self.gridSize-1, self.gridSize-1]

        # Call function to calculate limits if radius is not None
        if self.radius == None:
            self.calculateLimits()

    # Function to calculate limits for search
    def calculateLimits(self):
        """Calculate maximum radius for search."""
        # Calculate maximum distance between edge and x coordinate
        x_max = max(self.location[0], self.gridSize-1-self.location[0])
        # Calculate maximum distance between edge and y coordinate
        y_max = max(self.location[1], self.gridSize-1-self.location[1])
        # Set radius as max distance between current location and an edge
        self.radius = max(x_max, y_max)

    # Function to locate target
    def locateTarget(self):
        """Return target coordinates closest to location."""
        # Initialise target location
        targetLocation = None
        # Iterate from 0 to radius
        for i in range(self.radius+1):
            # Calculate search limits
            x_max = self.location[0] + i if self.location[0] + i < self.gridSize else self.gridSize - 1
            x_min = self.location[0] - i if self.location[0] > i else 0
            y_max = self.location[1] + i if self.location[1] + i < self.gridSize else self.gridSize - 1
            y_min = self.location[1] - i if self.location[1] > i else 0
            # Check top left edge for target
            if self.grid[x_min][y_min] == self.target:
                # Set target location
                targetLocation = (x_min, y_min)
                # Break from loop
                break
            # Check top right edge for target
            if self.grid[x_min][y_max] == self.target:
                # Set target location
                targetLocation = (x_min, y_max)
                # Break from loop
                break
            # Check bottom left edge for target
            if self.grid[x_max][y_min] == self.target:
                # Set target location
                targetLocation = (x_max, y_min)
                # Break from loop
                break
            # Check bottom right edge for target
            if self.grid[x_max][y_max] == self.target:
                # Set target location
                targetLocation = (x_max, y_max)
                # Break from loop
                break
            # Calculate limits
            lowerLimitY = self.location[1]-(i-1) if self.location[1] > (i-1) else 0
            upperLimitY = self.location[1]+(i-1) if self.location[1]+(i-1) < self.gridSize else self.gridSize - 1
            # Check cells in top and bottom edge
            for j in range(lowerLimitY, upperLimitY+1):
                if self.grid[x_min][j] == self.target:
                    # Set target location
                    targetLocation = (x_min, j)
                    # Break from loop
                    break
                if self.grid[x_max][j] == self.target:
                    # Set target location
                    targetLocation = (x_max, j)
                    # Break from loop
                    break
            # Calculate limits
            lowerLimitX = self.location[0]-(i-1) if self.location[0] > (i-1) else 0
            upperLimitX = self.location[0]+(i-1) if self.location[0]+(i-1) < self.gridSize else self.gridSize - 1
            # Check cells in left edge
            for j in range(lowerLimitX, upperLimitX+1):
                if self.grid[j][y_min] == self.target:
                    # Set target location
                    targetLocation = (j, y_min)
                    # Break from loop
                    break
                if self.grid[j][y_max] == self.target:
                    # Set target location
                    targetLocation = (j, y_max)
                    # Break from loop
                    break
            # Check if target location is obtained
            if not targetLocation == None:
                # Break from loop
                break
        # Return target
        return targetLocation
