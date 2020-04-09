#
# File containing code to calculate next sstep for players
#
#

# Function to calculate player's next step to reach target
def getNextStep(currentLocation, targetLocation):
    """Calculate next step to reach target.

    Keyword arguments:
    currentLocation -- tuple
    targetLocation -- tuple
    """
    # Initialise tuple for new location
    newLocation = [coordinate for coordinate in currentLocation]
    # check if parameters passed are tuples
    if type(currentLocation) == type((1,2)) and type(targetLocation) == type((1,2)):
        # Check if x coordinate needs to be incremented
        if currentLocation[0] < targetLocation[0]:
            newLocation[0] = currentLocation[0]+1
        # Check if x coordinate needs to be decremented
        elif currentLocation[0] > targetLocation[0]:
            newLocation[0] = currentLocation[0]-1
        # Check if y coordinate needs to be incremented
        if currentLocation[1] < targetLocation[1]:
            newLocation[1] = currentLocation[1]+1
        # Check if x coordinate needs to be decremented
        elif currentLocation[1] > targetLocation[1]:
            newLocation[1] = currentLocation[1]-1
    # TODO: throw error (parameters must of type tuple)
    # else:
    # Convert new location to tuple
    newLocation = tuple(newLocation)
    # Return new location
    return newLocation
