#
# File containing class for player
#
#

# Dependencies
import random
import string

# Local dependencies
from search import Search

# Initialise class
class Player:
    # Configure player
    def __init__(self):
        """Configure player with initial values."""
        # Set player id
        self.id = ''.join(random.choice(string.ascii_letters) for i in range(10))

        # Set player location
        self.location = None

        # Set hungry status to True
        self.hungry = True

        # initialise target
        self.target = None

        # Set safety status to True
        self.safety = True

        # Set terminate status to false
        self.terminate = False

    # Function to get player id
    def getId(self):
        """Return player id."""
        # Return id
        return self.id

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
    def nextTarget(self, grid):
        """Calculate next target of player by checking hunger status and safety status.

        Keyword arguments:
        grid -- Square matrix showing current state of grid
        """
        # Initialise variable to hold target
        target = None
        # Calculate grid size
        gridSize = len(grid)
        # Check if hungry flag is set to True
        if self.hungry:
            # Initialise search object for locating food
            search = Search(grid, self.location, 'F')
            # Get target
            target = search.start()
            print("inside hungry: ", "id: ", self.id, "target: ", self.target, "currTarget: ", target)
        else:
            # Call function to get the closest edge cell
            target = self.getClosestEdge(gridSize)
        # Check if target is set to None
        if target == None:
            # Iterate till a random target that is different from current location is obtained
            while True:
                # Get a random target
                target = (random.randint(0, gridSize-1), random.randint(0, gridSize-1))
                # Check if target and location are different
                if not target == self.location:
                    break
        # Update target
        self.setTarget(target)
        print("after setTarget: ", "id: ", self.id, "target: ", self.target)

    # Function to return the closest cdge cell
    def getClosestEdge(self, gridSize):
        """Calculate coordinates of closest cell in an edge.

        Keyword arguments:
        gridSize -- integer giving size of gird
        """
        # Initialise target variable
        target = None
        # Check magnitude of coordinates
        if self.location[0] > self.location[1]:
            # Check if both coordinates are greater than half grid size
            if self.location[1] > int(gridSize/2):
                target = (gridSize-1, self.location[1])
            # Check if both coordinates are smaller than half grid size
            elif self.location[0] < int(gridSize/2):
                target = (self.location[0], 0)
            # Handle case where one coordinate is greater than half grid size while other is smaller
            else:
                # Get the coordinate closer to edge
                if gridSize-1-self.location[0] > self.location[1]:
                    target = (self.location[0], 0)
                else:
                    target = (gridSize-1, self.location[1])
        else:
            # Check if both coordinates are greater than half grid size
            if self.location[0] > int(gridSize/2):
                target = (self.location[0], gridSize-1)
            # Check if both coordinates are smaller than half grid size
            elif self.location[1] < int(gridSize/2):
                target = (0, self.location[1])
            # Handle case where one coordinate is greater than half grid size while other is smaller
            else:
                # Get the coordinate closer to edge
                if gridSize-1-self.location[1] > self.location[0]:
                    target = (0, self.location[1])
                else:
                    target = (self.location[0], gridSize-1)
        # Return target tuple
        return target

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

    # Function to return current target
    def getTarget(self):
        """Return target tuple."""
        # Return target
        return self.target

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

    # Function to set safety status
    def setSafetyStatus(self, status):
        """Updates safety status to the boolean passed as parameter.

        Keyword arguments:
        status -- boolean indicating hunget status
        """
        # Check if status type is boolean
        if type(status) == type(False):
            # update hunger status
            self.safety = status

    # Function to get safety status
    def getSafetyStatus(self):
        """Returns safety status."""
        # Return safety status
        return self.safety

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

    # Function to set terminate flag to True
    def initiateTermination(self):
        """Change terminate flag value to True."""
        self.terminate = True

    # Function to get value of terminate flag
    def getTerminateStatus(self):
        """Return value of terminate flag."""
        return self.terminate
