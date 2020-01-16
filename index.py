#
# Index file
#
#

# Dependencies
from random import randint
from time import sleep
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
                "target" : {
                    "name" : 'F',
                    "coordinates": None
                },
                "food" : 0,
                "noOfSteps" : 8
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
        return tuple(pos)

    # Function to add player locations to grid
    def updateGrid(self):
        """Reset cells in grid and set player locations"""
        # Get lock for grid
        lock = threading.RLock()
        lock.acquire()
        # Initialise variable to hold food coordinates
        food = []
        # Set all cell to 0
        for i in range(self.gridSize):
            for j in range(self.gridSize):
                # Store food coordinates
                if self.grid[i][j] == 'F':
                    food.append((i, j))
                # Mark boundaires as home
                if i == 0:
                    self.grid[i][j] = 'H'
                elif i == self.gridSize-1:
                    self.grid[i][j] = 'H'
                elif j == 0:
                    self.grid[i][j] = 'H'
                elif j == self.gridSize-1:
                    self.grid[i][j] = 'H'
                else:
                    self.grid[i][j] = 0

        # Set food locations
        for foodItem in food:
            self.grid[foodItem[0]][foodItem[1]] = 'F'

        # Update grid to display all players
        for playerId in self.players.keys():
            self.grid[self.players[playerId]["pos"][0]][self.players[playerId]["pos"][1]] = 'P'

        # Release lock on grid
        lock.release()

    # Function to display grid
    def displayGrid(self):
        """Print grid"""
        # Iterate over grid
        for row in self.grid:
            for element in row:
                print(element, end="")
            print()

    # Function to move player
    def movePlayer(self, playerId):
        """Get target and move player one step closer to target

        Keyword arguments:
        playerId -- String to identify each player"""
        # Get lock for grid
        lock = threading.RLock()
        lock.acquire()

        for i in range(self.players[playerId]["noOfSteps"]):
            # Initialise search object
            search = Search(self.grid, self.players[playerId]["pos"], self.players[playerId]["target"]["name"])
            # Get and update player target
            self.players[playerId]["target"]["coordinates"] = search.start()

            # Move player towards target
            new_x = self.players[playerId]["pos"][0]
            new_y = self.players[playerId]["pos"][1]

            # calculate new position
            if self.players[playerId]["pos"][0] > self.players[playerId]["target"]["coordinates"][0]:
                new_x = self.players[playerId]["pos"][0]-1
            elif self.players[playerId]["pos"][0] < self.players[playerId]["target"]["coordinates"][0]:
                new_x = self.players[playerId]["pos"][0]+1

            if self.players[playerId]["pos"][1] > self.players[playerId]["target"]["coordinates"][1]:
                new_y = self.players[playerId]["pos"][1]-1
            elif self.players[playerId]["pos"][1] < self.players[playerId]["target"]["coordinates"][1]:
                new_y = self.players[playerId]["pos"][1]+1

            # Update player position
            self.players[playerId]["pos"] = (new_x, new_y)

            # Check if player reached target
            if self.players[playerId]["pos"] == self.players[playerId]["target"]["coordinates"]:
                # Check if target is food
                if self.players[playerId]["target"]["name"] == 'F':
                    # Update food count
                    self.players[playerId]["food"] = self.players[playerId]["food"] + 1
                    # Remove food from cell
                    self.grid[new_x][new_y] = 0
                    # Switch target to home
                    self.players[playerId]["target"]["name"] = 'H'
                # Check if target is home
                elif self.players[playerId]["target"]["name"] == 'H':
                        # Exit loop
                        break

        self.updateGrid()

        lock.release()

    # Start function
    def start(self):
        """Initialise thread for each player and start thread"""
        # Iterate over players
        for playerId in self.players.keys():
            newThread = threading.Thread(target=self.movePlayer, args=[playerId])
            newThread.start()

eco = Ecosystem()
eco.initialiseFood()
eco.displayGrid()
eco.start()
print("---")
# Wait for threads to finish execution
while threading.active_count() > 1:
    sleep(3)
# Update Grid with new positions
eco.updateGrid()
eco.displayGrid()
print("---")
