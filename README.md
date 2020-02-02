# game-of-life
By Daniel Pan  
Conway's game of life implemented in Python

The screen is laid out on a grid, with each square in the grid representing a cell.

The cells follow three rules:  
	1. If there are 1 or less live neighbors, the cell dies  
	2. If there are 2 or 3 live neighbors, the cell stays alive  
	3. If there are more than 3 live neighbors, the cell dies  
	4. If there are exactly 3 live neighbors, a dead cell will become alive

These rules can give rise to many complex patterns and graphics.

Usage:  
At command line, run gameoflife.py with two arguments: length and width.  
Due to spacing of output, length is automatically divided by 2 so that calling with equal length and width will output a square.  
Make sure your terminal is large enough to output the board size.