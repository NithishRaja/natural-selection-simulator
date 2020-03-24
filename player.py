#
# File containing test player logic
#
#

# Dependencies
import random
import string

# Initialise class
class Player:
    # Initialise constructor
    def __init__(self):
        """Set default value to config parametes."""
        # Initialise player id
        self.id = ''.join(random.choice(string.ascii_letters) for i in range(10))

        # Initialise player location
        self.location = None

        # Initialise hunger status
        self.hunger = True

        # Initialise safety status
        self.safety = True

    # Function to get player id
    def getId(self):
        """Return player id."""
        return self.playerId

    # Function to get player location
    def getLocation(self):
        """Return location."""
        return self.location

    # Function to update player location
    def updateLocation(self, location):
        """Set location to given location parameter.

        Keyword arguments:
        location -- tuple
        """
        # Check if location paramenter is a tuple
        if type(location) == type((1,2)):
            # Update location
            self.location = location
        # TODO: throw error (passed parameter is not a tuple)
        # else:
