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
            print(row)

    

eco = Ecosystem()
eco.initialiseFood()
eco.displayGrid()
