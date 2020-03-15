#
# Test file
#
#

# Dependencies

# Local dependencies
from grid import Grid
from player import Player

# Set grid size
gridSize = 10

# Initialise grid object
grid = Grid(gridSize)

# Initialise player
player1 = Player()

# Place player on grid
grid.playerStart(player1)

# Print grid
grid.displayGrid()

# Print player location
print("location: ", player1.location)

# Calculate player target
player1.nextTarget(grid.getGrid())

# Print player target
print("target: ", player1.target)

counter = 0

while True:
    if not player1.getHungerStatus():
        if player1.getSafetyStatus():
            break
    # Update player target
    player1.nextTarget(grid.getGrid())
    # Move player towards target
    grid.movePlayer(player1.getId(), player1.getLocation(), player1.getNextStep())
    print("---")
    # Print grid
    grid.displayGrid()
    # Update number of moves
    counter = counter+1
    if counter > 11:
        break
