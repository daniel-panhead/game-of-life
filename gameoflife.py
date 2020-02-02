# By Daniel Pan

import random
import curses
import time

def generateGrid(l, w):
	grid = []
	# down
	for i in range(l):
		row = []
		# across
		for j in range(w):
			row.append(random.randint(0, 1))
		grid.append(row)
	return grid

def printGrid(gridArr):
	i = 0
	for row in gridArr:
		rowStr = ""
		for cell in row:
			if(cell == 1):
				rowStr += "#"
			else:
				rowStr += " "
		stdscr.addstr(i, 0, rowStr)
		#stdscr.addstr(i, 0, "  ".join("{0}".format(n) for n in row))
		i += 1
	stdscr.refresh()

def checkNeighbors(gridArr, rowArr, cellIndex, rowIndex):
	alive = 0
	dead = 0

	# check one behind
	if(cellIndex == 0): pass
	else:
		if(rowArr[cellIndex-1] == 1): alive += 1
		elif(rowArr[cellIndex-1] == 0): dead +=1

	# check one above behind
	if(cellIndex == 0 or rowIndex == 0): pass
	else:
		if(gridArr[rowIndex-1][cellIndex-1] == 1): alive += 1
		elif(gridArr[rowIndex-1][cellIndex-1] == 0): dead +=1

	# check one below behind
	if(cellIndex == 0): pass
	else:
		try:
			if(gridArr[rowIndex+1][cellIndex-1] == 1): alive += 1
			elif(gridArr[rowIndex+1][cellIndex-1] == 0): dead +=1
		except IndexError: pass

	# check one in front
	try:
		if(rowArr[cellIndex+1] == 1): alive += 1
		elif(rowArr[cellIndex+1] == 0): dead +=1
	except IndexError: pass

	# check one above front
	try:
		if(rowIndex == 0): pass
		else:
			if(gridArr[rowIndex-1][cellIndex+1] == 1): alive += 1
			elif(gridArr[rowIndex-1][cellIndex+1] == 0): dead +=1
	except IndexError: pass

	# check one below front
	try:
		if(gridArr[rowIndex+1][cellIndex+1] == 1): alive += 1
		elif(gridArr[rowIndex+1][cellIndex+1] == 0): dead +=1
	except IndexError: pass


	# check one above
	if(rowIndex == 0): pass
	else:
		if(gridArr[rowIndex-1][cellIndex] == 1): alive += 1
		elif(gridArr[rowIndex-1][cellIndex] == 0): dead +=1

	# check one below
	try:
		if(gridArr[rowIndex+1][cellIndex] == 1): alive += 1
		elif(gridArr[rowIndex+1][cellIndex] == 0): dead +=1
	except IndexError: pass

	return alive

def checkLiveState(alive):
	# 0 or 1 live neighbors becomes dead
	if(alive <= 1): return 0
	# 2 or 3 live neighbors stays alive
	if(alive == 2 or alive == 3): return 1
	# more than 3 live neighbors becomes dead
	if(alive > 3): return 0
	# wtf happened
	return -1

def checkDeadState(alive):
	# exactly three live neighbors becomes alive
	if(alive == 3): return 1
	else: return 0

def modifyState(gridArr):
	retArr = []
	for rowIndex in range(len(gridArr)): # y
		rowArr = []
		for cellIndex in range(len(gridArr[rowIndex])): # x
			aliveNeighbors = checkNeighbors(gridArr, gridArr[rowIndex], cellIndex, rowIndex)
			currentCell = gridArr[rowIndex][cellIndex]

			if(currentCell == 1):
				currentCell = checkLiveState(aliveNeighbors)
			elif(currentCell == 0):
				currentCell = checkDeadState(aliveNeighbors)

			rowArr.append(currentCell)
		retArr.append(rowArr)
	return retArr

if __name__ == "__main__":
	stdscr = curses.initscr()
	curses.noecho()
	curses.cbreak()

try:
	grid = generateGrid(30, 30)
	while True:
		printGrid(grid)
		grid = modifyState(grid)
		time.sleep(0.05)
finally:
	curses.echo()
	curses.nocbreak()
	curses.endwin()
