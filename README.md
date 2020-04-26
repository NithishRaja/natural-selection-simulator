# NATURAL SELECTION SIMULATOR

* A simple program to simulate natural selection.
* The program tries to reproduce the results in this [video](https://www.youtube.com/watch?v=0ZGbIKd0XrM)

## Editing code

* `index.py` is the entry file
* Logic for player grid interaction is in `ecosystem.py` file
* Code for the grid is in `grid/grid.py`
* The grid consists of multiple cells
* Code for cells is in `grid/cell.py`
* Code for players is in `player.py`
* The search algorithm used is in `search.py`

## Running program

* Create a **logging** directory in root
* Run `python index.py` in root

## Configuration

### Grid configuration

* Configurations for the grid can be changed by modifying the **gridConfig.json** file
* Parameters such as `gridSize`, `foodLimit`, `noOfPlayers`, `noOfDays`, `baseLogDir` can be updated in grid config

### Player configuration

* Player configurations can be changed by modifying the **defaultPlayerConfig.json** file

## Logging

* Grid state for each day is logged inside **logging/day{day no}/grid**
* Grid state is written to file as a matrix with each cell indicating its status
* All movements in the grid is logged inside **logging/day{day no}/gridMovements** in order of their occurrence
* The grid movements are written in the following format: playerId, current_x, current_y, new_x, new_y
* Player movements for each day is logged inside **logging/day{day no}/{player id}**
* Each player movement is written in the following format: hunger, safety, current_x, current_y, target_x, target_y, new_x, new_y
* Player configurations is logged inside **logging/day{day no}/playerConfig**
* Player configuration is written in the following format: id, movement limit, vision limit, recharge duration

## Features

* Threads are assigned a player and has to move player to collect food and return back to a safe cell
* Player movements are limited by vision limit, movement limit and recharge duration
* Vision limit - puts a limit on the search radius
* Movement limit - limits the number of steps taken by the player
* Recharge duration - duration for which player has to wait after each movement
* If target cannot be located, a random target is chosen and search for target continues at each step
* Players have a chance to reproduce at end of each cycle
* Chance for reproduction increases till player does reproduces, after reproduction the chance gets reset to 0

## Docker

* The docker image can be found at [docker hub](https://hub.docker.com/repository/docker/nithishraja/natural_selection_simulator)
* Instructions on how to use the image are also at [docker hub](https://hub.docker.com/repository/docker/nithishraja/natural_selection_simulator)
