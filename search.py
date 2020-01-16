#
# File containing code to perform grid search
#
#

# Dependencies


# initialise class
class Search:
    # Initialise values
    def __init__(self, grid, startingPoint, searchTarget):
        """Store grid, starting point and search target

        Keyword arguments:
        grid -- Square matrix to  perform search on
        startingPoint -- Tuple with the starting point for search
        searchTarget -- String or Integer with the search target
        """
        # Set grid
        self.grid = grid

        # Set grid size
        self.gridSize = len(self.grid)

        # Set starting point
        self.startingPoint = startingPoint

        # Set search target
        self.searchTarget = searchTarget

    # Initialise function to perform search
    def start(self):
        """Perform grid search and return the result"""
        # Initialise limits for searching
        x_low = None
        y_low = None
        x_high = None
        y_high = None

        # Array to hold all cells already searched
        old = []

        # Initialise search radius
        searchRadius = 0

        # Flag to indicate status of search
        found = False

        # Initialising food location
        foodLocation = None

        # Perform grid search to locate food
        while not found:
            # Update search radius
            searchRadius = searchRadius + 1
            # Check if all cells have been searched
            if (self.gridSize-1, self.gridSize-1) in old:
                if (0, 0) in old:
                    break
            else:
                # Get limiting cell coordinates for given search radius
                x_low = self.startingPoint[0]-searchRadius if self.startingPoint[0]-searchRadius > 0 else 0
                y_low = self.startingPoint[1]-searchRadius if self.startingPoint[1]-searchRadius > 0 else 0

                x_high = self.startingPoint[0]+searchRadius if self.startingPoint[0]+searchRadius < self.gridSize-1 else self.gridSize-1
                y_high = self.startingPoint[1]+searchRadius if self.startingPoint[1]+searchRadius < self.gridSize-1 else self.gridSize-1

                # Search all cells in guven search radius
                for j in range(x_low, x_high+1):
                    for k in range(y_low, y_high+1):
                        # If cell was searched before, ignore it
                        if (j, k) in old:
                            break
                        elif self.grid[j][k] == 'F':
                            found=True
                            foodLocation = (j, k)
                            break
                    if found:
                        break
        # Return the food location
        # print("player position: ", self.startingPoint, " closest food location: ", foodLocation)
        return foodLocation
