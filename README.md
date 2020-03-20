# NATURAL SELECTION SIMULATOR

* A simple program to simulate natural selection.
* The program tries to reproduce the results in this [video](https://www.youtube.com/watch?v=0ZGbIKd0XrM)

## Editing code

* `index.py` is the entry file
* Code for the grid is in `grid.py`
* Code for players is in `player.py`
* The search algorithm used is in `search.py`

## Running program

* Create a **logging** directory in root
* Run `python index.py` in root

## Logging

* grid state for each day is logged inside **logging/day{day no}**
* player movements for each day is logged inside **logging/day{day no}/{player id}**

## Features

* Currently a new grid is being worked on where all cells are objects instead of some being strings and others being arrays
