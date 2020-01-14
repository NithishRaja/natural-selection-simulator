#
# Index file
#
#

# Dependencies
from random import randint
import threading

# Local dependencies
from search import Search

# Initialise class
class Ecosystem:
    # Function to initialise ecosystem
    def __init__(self):
        """Initialise grid and starting players"""

        # Initialise grid
        self.grid = []

        # Set grid size
        self.gridSize = 10

        # Initialise players
        self.players = {}

        # Set no of players
        self.noOfPlayers = 2

        # Initialise player id counter
        self.playerIdCounter = 0

        # Initialise array to hold food locations
        self.food = []

        # Set food limit
        self.foodLimit = 10

        # Call function to initialise grid
        self.initialiseGrid()

        # Call function to initialise players
        self.initialisePlayers()

        # Update grid to reflect new players
        self.updateGrid()

    # Function to initialise grid and set players
    def initialiseGrid(self):
        """Initialise grid positions with 0 and place players on grid"""
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
            self.players[str(self.playerIdCounter)] = {
                "id" : self.playerIdCounter,
                "pos" : tuple(pos),
                "target" : None
            }
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
        """Return position of an empty cell along the edges of the grid

        keyword arguments:
        food -- flag mentioning location for food or for player
        """
        # Initialise array to hold position
        pos = [None, None]
        # Get starting location for new player
        while True:
            if food:
                pos[0] = randint(1, self.gridSize-2)
                pos[1] = randint(1, self.gridSize-2)
            else:
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
        for playerId in self.players.keys():
            self.grid[self.players[playerId]["pos"][0]][self.players[playerId]["pos"][1]] = 'P'

    # Function to display grid
    def displayGrid(self):
        """Print grid"""
        # Iterate over grid
        for row in self.grid:
            for element in row:
                print(element, end="")
            print()

    # Start function
    def start(self):
        """Initialise thread for each player and start thread"""
        # Iterate over players
        for playerId in self.players.keys():
            locate = Search(self.grid, self.players[playerId]["pos"], 'F')
            newThread = threading.Thread(target=locate.start)
            newThread.start()

eco = Ecosystem()
eco.initialiseFood()
eco.displayGrid()
eco.start()
