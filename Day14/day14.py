def MakeGrid(filename):
    grid = []
    with open('input.txt', 'r') as f:
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

def SlideWest():
    pass

def SlideSouth():
    pass

def SlideEast():
    pass

def NorthLoad(grid):
    load = 0
    for i, row in enumerate(grid):
        load += len([c for c in row if c == 'O']) * (len(grid)-i)
    return load

def Day14():
    grid = MakeGrid('input.txt')
    SlideNorth(grid)
    load = NorthLoad(grid)
    print(f'Load={load}')


Day14()