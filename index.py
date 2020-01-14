#
# Index file
#
#

# Dependencies
from random import randint

# Initialise class
class Ecosystem:
    # Function to initialse ecosystem
    def __init__(self):
        """Initialse grid and starting players"""

        # Initialise grid
        self.grid = []

        # Set grid size
        self.gridSize = 10

        # Initialise players
        self.players = []

        # Set no of players
        self.noOfPlayers = 2

        # Initialse player id counter
        self.playerIdCounter = 0

        # Initialise array to hold food locations
        self.food = []

        # Set food limit
        self.foodLimit = 10

        # Call function to initialise grid
        self.initialiseGrid()

        # Call function to initialse players
        self.initialisePlayers()

        # Update grid to reflect new players
        self.updateGrid()

    # Function to initialse grid and set players
    def initialiseGrid(self):
        """Initialse grid positions with 0 and place players on grid"""
        # Iterate over grid
        for i in range(self.gridSize):
            self.grid.append([])
            for j in range(self.gridSize):
                self.grid[i].append(0)

    # Function to add players
    def initialisePlayers(self):
        """Initialise players with an id number and a starting position"""
        # initialise new players
        for i in range(self.noOfPlayers):
            pos = self.getNewPosition()
            # Set id and starting position for all players
            self.players.append({
                "id" : self.playerIdCounter,
                "pos" : tuple(pos)
            })
            # Update player id number
            self.playerIdCounter = self.playerIdCounter + 1

    # Function to place food on grid
    def initialiseFood(self):
        """Randomly place food on grid till food limit is reached"""
        # Iterate till food limit
        for i in range(self.foodLimit):
            # Get new position for food
            pos = self.getNewPosition(food=True)
            # Append position to food array
            self.food.append(pos)
            # Update grid
            self.grid[pos[0]][pos[1]] = 'F'

    # Function to assign an empty cell along edge to players
    def getNewPosition(self, food=False):
        """Return position of an empty cell along the edges of the grid"""
        # Initialse array to hold position
        pos = [None, None]
        # Get starting location for new player
        while True:
            if food:
                pos[0] = randint(1, self.gridSize-2)
                pos[1] = randint(1, self.gridSize-2)
            else:
                # Get new positions
                pos[0] = randint(0, self.gridSize-1)
                pos[1] = randint(0, 1)*(self.gridSize-1)
                # Reverse position of list to allow players to start along y axis
                if randint(1, 100)%2 == 0:
                    pos.reverse()
            # Check if new position is empty
            if self.grid[pos[0]][pos[1]] == 0:
                break
        return pos

    # Function to add player locations to grid
    def updateGrid(self):
        """Reset cells in grid and set player locations"""
        # Remove all food
        self.food = []
        # Update grid to display all players
        for plyr in self.players:
            self.grid[plyr["pos"][0]][plyr["pos"][1]] = 'P'

    # Function to display grid
    def displayGrid(self):
        """Print grid"""
        # Iterate over grid
        for row in self.grid:
            for element in row:
                print(element, end="")
            print()

    # Function to search food
    def search(self, player):
        """Perform grid search to locate food nearest to player"""
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
                x_low = player["pos"][0]-searchRadius if player["pos"][0]-searchRadius > 0 else 0
                y_low = player["pos"][1]-searchRadius if player["pos"][1]-searchRadius > 0 else 0

                x_high = player["pos"][0]+searchRadius if player["pos"][0]+searchRadius < self.gridSize-1 else self.gridSize-1
                y_high = player["pos"][1]+searchRadius if player["pos"][1]+searchRadius < self.gridSize-1 else self.gridSize-1

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
        return foodLocation

eco = Ecosystem()
eco.initialiseFood()
eco.displayGrid()
