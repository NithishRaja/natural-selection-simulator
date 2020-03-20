#
# File containing code for cell
#
#

# Dependencies

# Initialise class
class Cell:
    # Initialise constructor
    def __init__(self):
        """Set default values for food, safe and players."""
        # Initialise food variable
        self.food = 0

        # Initialise safe variable
        self.safe = False

        # Initialise array to hold players
        self.players = []

    # Function to check if food exists
    def foodExists(self):
        """Return True if food is positive else return False."""
        # Check if food is above 0
        if food > 0:
            # return True
            return True
        else:
            return False

    # Function to check if cell is safe
    def isSafe(self):
        """Return value of safe variable."""
        return self.safe

    # Function to update safety status of cell
    def updateSafety(self, safe):
        """Set value of safe variable to the boolean passed.

        Keyword arguments:
        safe -- boolean representing whether cell is safe or not
        """
        # Check is paramenter is a boolean
        if type(safe) == type(True):
            # Set safety to passed value
            self.safe = safe
        # TODO: log an error when trying to update cell safety (passed parameter is not a boolean)
        # else:

    # Function to get number of players
    def getPopulation(self):
        """Return the size of players array."""
        return len(self.players)