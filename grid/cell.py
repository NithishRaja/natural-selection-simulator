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
        if self.food > 0:
            # return True
            return True
        else:
            return False

    # Function to modify food value
    def modifyFoodCount(self, modification):
        """Increment, decrement or reset to zero food value according to parameter.

        Keyword arguments:
        modification -- one of three strings in 'increment', 'decrement' or 'reset'
        """
        # Check if modification is among allowed modifications
        if modification in ["increment", "decrement", "reset"]:
            # Check if modification is increment
            if modification == "increment":
                # Increase food value by 1
                self.food = self.food + 1
                # Return True
                return True
            # Check if modification is decrement
            if modification == "decrement":
                # Check if food value is positive
                if self.food > 0:
                    # Decrease food value
                    self.food = self.food - 1
                    # Return True
                    return True
                else:
                    # Food value is zero or below zero
                    return False
            # Check if modification is reset
            if modification == "reset":
                # Set food value to zero
                self.food = 0
                # Return True
                return True
        # TODO: log error trying to update cell food count (attempted modification not allowed)
        # else:

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

    # Function to add players to cell
    def addPlayer(self, player):
        """Append player to players array.

        Keyword arguments:
        player -- player object
        """
        self.players.append(player)

    # Function to remove player from cell by player id
    def removePlayer(self, playerId):
        """Remove player with given id from array and return player else return False.

        Keyword arguments:
        playerId -- String
        """
        # Initialise index for player
        playerIndex = None
        # Iterate over all players
        for index, player in enumerate(self.players):
            # Check if player with requested id exists
            if player.getId() == playerId:
                # Set player index to current index
                playerIndex = index
                # Exit loop
                break
        # Check if player index is set
        if type(playerIndex) == type(1):
            # Remove player from array
            player = self.players.pop(playerIndex)
            # Return player
            return player
        else:
            # Player does not exist, return False
            return False

    # Function to get number of players
    def getPopulation(self):
        """Return the size of players array."""
        return len(self.players)
