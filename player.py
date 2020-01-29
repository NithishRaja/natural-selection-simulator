#
# File containing class for player
#
#

# Local dependencies
from search import Search

# Initialise class
class Player:
    # Configure player
    def __init__(self):
        """Configure player with initial values."""
        # Set player location
        self.location = None

        # Set hungry status to true
        self.hungry = True

        # initialise target
        self.target = None

    # Function to set current location
    def setLocation(self, location):
        """Set current location of player.

        Keyword arguments:
        location -- tuple with x and y coordinates
        """
        # Check if location is a tuple
        if type(location) == type(tuple([1, 2])):
            # Set current location
            self.location = location

    # Function to set current location
    def getLocation(self):
        """Return current location of player."""
        # Return player location
        return self.location

    # Function to get target for player
    def getTarget(self, grid):
        # Check if hungry flag is set to True
        if self.hungry:
            # Initialise search object for locating food
            search = Search(grid, self.location, 'F')
        else:
            # Initialise search object for locating edge
            search = Search(grid, self.location, 'H')
        # Update target
        self.setTarget(search.start())

    # Function to set target
    def setTarget(self, target):
        """Set target for player.

        Keyword arguments:
        target -- tuple with x and y coordinates
        """
        # Check if target is a tuple
        if type(target) == type(tuple([1, 2])):
            # Set current target
            self.target = target

    # Function to set hunger status
    def setHungerStatus(self, status):
        """Updates hunger status to the boolean passed as parameter.

        Keyword arguments:
        status -- boolean indicating hunget status
        """
        # Check if status type is boolean
        if type(status) == type(False):
            # update hunger status
            self.hungry = status

    # Function to get hunger status
    def getHungerStatus(self):
        """Returns hunger status."""
        # Return hunger status
        return self.hungry

    # Function to move player
    def getNextStep(self):
        """Returns coordinates of the cell closest to location along target direction."""
        # Initialise variable for new x and y coordinates
        x_new = self.location[0]
        y_new = self.location[1]

        # calculate new x coordinate
        if self.target[0] < self.location[0]:
            x_new = self.location[0]-1
        elif self.target[0] > self.location[0]:
            x_new = self.location[0]+1

        # calculate new y coordinate
        if self.target[1] < self.location[1]:
            y_new = self.location[1]-1
        elif self.target[1] > self.location[1]:
            y_new = self.location[1]+1

        return (x_new, y_new)
