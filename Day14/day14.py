import copy

def MakeGrid(filename):
    grid = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            grid.append([])
            for c in line:
                grid[-1].append(c)
    return grid

def PrintGrid(grid):
    for row in grid:
        for cell in row:
            print(cell, end='')
        print()
    print()

def SlideNorth(grid):
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == 'O':
                newY = y
                for i in range(y-1, -1, -1):
                    if grid[i][x] == '.':
                        newY = i
                    else:
                        break
                if newY != y:
                    grid[newY][x] = 'O'
                    grid[y][x] = '.'

def SlideWest(grid):
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == 'O':
                newX = x
                for i in range(x-1, -1, -1):
                    if grid[y][i] == '.':
                        newX = i
                    else:
                        break
                if newX != x:
                    grid[y][newX] = 'O'
                    grid[y][x] = '.'

def SlideSouth(grid):
    for y, row in reversed(list(enumerate(grid))):
        for x, cell in enumerate(row):
            if cell == 'O':
                newY = y
                for i in range(y+1, len(grid)):
                    if grid[i][x] == '.':
                        newY = i
                    else:
                        break
                if newY != y:
                    grid[newY][x] = 'O'
                    grid[y][x] = '.'

def SlideEast(grid):
    for y, row in enumerate(grid):
        for x, cell in reversed(list(enumerate(row))):
            if cell == 'O':
                newX = x
                for i in range(x+1, len(row)):
                    if grid[y][i] == '.':
                        newX = i
                    else:
                        break
                if newX != x:
                    grid[y][newX] = 'O'
                    grid[y][x] = '.'    

def DoCycle(grid):
    SlideNorth(grid)
    SlideWest(grid)
    SlideSouth(grid)
    SlideEast(grid)

def NorthLoad(grid):
    load = 0
    for i, row in enumerate(grid):
        load += len([c for c in row if c == 'O']) * (len(grid)-i)
    return load

def Day14():
    # # Part 1
    # SlideNorth(grid)
    # load = NorthLoad(grid)
    # print(f'Load={load}')

    # # Brute force while we work out a proper solution...
    # grid = MakeGrid('input.txt')
    # for i in range(1000000000):
    #     DoCycle(grid)
    #     if i % 10000 == 0:
    #         print(f'{(i/1000000000) * 100}% done')
    # PrintGrid(grid)
    # result = NorthLoad(grid)
    # print(f'Load = {result}')

    # For this to be quickly solvable, there needs to be a point where the rocks get into a 
    # repeating pattern. Store the results of multiple cycles and try to find it
    grid = MakeGrid('input.txt')
    history = [grid]
    for i in range(1000): # arbitrary, seems big enough...
        DoCycle(grid)
        history.append(copy.deepcopy(grid))        
        if (i+1) % 100 == 0:
            print(f'Done {i+1}')

    matches = {}
    for i in range(1, len(history)//2):
        matches[i] = 0
        print(f'Looking for periods of length {i}')
        for j in range(len(history)-i):
            if history[j] == history[j+i]:
                matches[i] += 1

    # Assuming we've simulated a long enough period, the value with the most
    # matches should be the correct period
    periods = list(matches.items())
    periods.sort(key=lambda x: x[1], reverse=True)
    period = periods[0][0]
    print(f'Period = {period}')

    # We also need to find the point at which the period starts
    offset = -1
    for i in range(len(history)-period):
        if history[i:i+period] == history[i+period:i+(2*period)]:
            offset = i
            break
    print(f'Offset = {offset}')

    # Now we can just get the result from the stored states
    equivalentIndex = (1000000000 % period)
    while equivalentIndex < offset:
        equivalentIndex += period
    print(f'Index = {equivalentIndex}')
    result = NorthLoad(history[equivalentIndex])
    print(f'Result = {result}')

Day14()