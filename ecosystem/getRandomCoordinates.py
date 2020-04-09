#
# File containing code to generate random coordinates
#
#

# Dependencies
import random

# Function to get random coordinates
def getRandomCoordinates(gridSize):
    """Generate random coordinates within grid.

    Keyword arguments:
    gridSize -- integer
    """
    # Generate random coordinates
    coordinates = (random.randint(0, gridSize-1), random.randint(0, gridSize-1))
    # Return coordinates
    return coordinates
