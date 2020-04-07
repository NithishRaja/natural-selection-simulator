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

## Logging

* Grid state for each day is logged inside **logging/day{day no}/grid**
* All movements in the grid is logged inside **logging/day{day no}/gridMovements** in order of their occurrence
* Player movements for each day is logged inside **logging/day{day no}/{player id}**

## Features

* Threads are assigned a player and has to move player to collect food and return back to a safe cell
* Player movements are limited by vision limit, movement limit and recharge duration
* Vision limit - puts a limit on the search radius
* Movement limit - limits the number of steps taken by the player
* Recharge duration - duration for which player has to wait after each movement
* If target cannot be located, a random target is chosen and search for target continues at each step
