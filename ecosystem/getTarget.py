#
# File containing code to calculate target
#
#

# Function to get player target
def getTarget(hungerStatus, safetyStatus):
    """Get player target based on player status.

    Keyword arguments:
    hungerStatus -- boolean
    safetyStatus -- boolean
    """
    # Initialise target
    target = None
    # Check if hungerStatus and safetyStatus are boolean
    if type(hungerStatus) == type(True) and type(safetyStatus) == type(True):
        # Check hunger status of player
        if hungerStatus:
            # Set player target to food
            target = "food"
        # Check safety status of player
        elif not safetyStatus:
            # Set player target to home
            target = "home"
    # Return target
    return target
