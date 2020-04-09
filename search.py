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
        # Initialise array to hold coordinates of cells to search
        searchTargets = []
        # Append current location to search targets
        searchTargets.append(self.location)
        # Iterate till search radius is reached
        for i in range(self.radius+1):
            # Iterate over all elemnts in search targets
            for coordinate in searchTargets:
                # Check if target exists in current coordinate
                if self.grid[coordinate[0]][coordinate[1]] == self.target:
                    # Update target location
                    targetLocation = coordinate
                    # Break from loop
                    break
            # Empty search targets
            searchTargets = []
            # Calculate minimum and maximum coordinate values of neighbour cells
            x_max = self.location[0] + 1 if self.location[0] + 1 < self.gridSize else self.gridSize - 1
            x_min = self.location[0] - 1 if self.location[0] > 1 else 0
            y_max = self.location[1] + 1 if self.location[1] + 1 < self.gridSize else self.gridSize - 1
            y_min = self.location[1] - 1 if self.location[1] > 1 else 0
            # Iterate over all neighbour cells above and below
            for y in range(y_min, y_max+1):
                # Add neighbour cells below coordinate to search targets
                searchTargets.append((x_min, y))
                # Add neighbour cells below coordinate to search targets
                searchTargets.append((x_max, y))
            # Iterate over all neighbour cells to left and right
            for x in range(x_min+1, x_max):
                # Add neighbour cells to left of coordinate to search targets
                searchTargets.append((x, y_min))
                # Add neighbour cells to right of coordinate to search targets
                searchTargets.append((x, y_max))
        # Return target
        return targetLocation
