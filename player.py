#
# File containing class for player
#
#

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
        """Set current location of playerself.

        Keyword arguments:
        location -- tuple with x and y coordinates
        """
        # Check if location is a tuple
        if type(location) == type(tuple([1, 2])):
            # Set current location
            self.location = location

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
