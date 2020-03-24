#
# Test file
#
#

# Dependencies
import json
import random

# Local dependencies
from testPlayer import Player
from testSearch import Search

# Local dependencies
from grid.grid import Grid

# Read grid config from file
file = open("./gridConfig.json")
gridConfig = json.load(file)

# initialise grid with grid size
grid = Grid(gridConfig["gridSize"])

# Initialise food on grid
grid.initialiseFood(gridConfig["foodLimit"])

# Initialise array to hold players
players = []

# Create player objects and append them to players array
for i in range(gridConfig["noOfPlayers"]):
    players.append(Player())

# Iterate over players and add them to grid
for player in players:
    # Initialise coordinate
    coordinate = None
    # Choose a random coordinate
    toss = random.randint(1,2)
    if toss == 1:
        coordinate = (random.randint(0, gridConfig["gridSize"]-1), random.randint(0, 1)*(gridConfig["gridSize"]-1))
    else:
        coordinate = (random.randint(0, 1)*(gridConfig["gridSize"]-1), random.randint(0, gridConfig["gridSize"]-1))
    # Update location for player
    player.updateLocation(coordinate)
    # Add player to coordinate
    grid.grid[coordinate[0]][coordinate[1]].addPlayer(player)

# Get snapshot of grid
snapshot = grid.getSnapshot("food")

# Print snapshot of grid
# Iterate over each row
for i in range(gridConfig["gridSize"]):
    # Iterate over each column
    for j in range(gridConfig["gridSize"]):
        # Print cell
        print(snapshot[i][j], end="\t")
    # Enter new line for each row
    print()

for player in players:
    print(player.getLocation())
    search = Search(snapshot, player.getLocation(), "F", None)
    print("---")
    target = search.locateTarget()
    print("---")
    print(target)
