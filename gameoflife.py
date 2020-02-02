# By Daniel Pan

import random
import curses

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
	# for row in gridArr:
	# 	# stdscr.addstr(i, 0, "  ".join("{0}".format(n) for n in row))
	# 	stdscr.addstr(i, 0, "Hello")
	# 	i += 1
	stdscr.addstr(0, 0, "Hello")
	stdscr.addstr(1, 0, "World")
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
	for rowIndex in range(len(gridArr)):
		rowArr = []
		for cellIndex in range(len(gridArr[rowIndex])):
			aliveNeighbors = checkNeighbors(gridArr, gridArr[rowIndex], cellIndex, rowIndex)
			# print("[" + str(rowIndex) + "][" + str(cellIndex) + "]" + " ")
			# print(aliveNeighbors)
			# print()

			cell = gridArr[rowIndex][cellIndex]

			if(cell == 1):
				cell = checkLiveState(aliveNeighbors)
			elif(cell == 0):
				cell = checkDeadState(aliveNeighbors)
			rowArr.append(cell)
		retArr.append(rowArr)
	return retArr

if __name__ == "__main__":
	stdscr = curses.initscr()
	curses.noecho()
	curses.cbreak()

try:
	grid = generateGrid(4, 4)
	printGrid(grid)

	grid = modifyState(grid)
finally:
	curses.echo()
	curses.nocbreak()
	curses.endwin()
