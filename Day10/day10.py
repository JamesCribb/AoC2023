allDirs = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']

directions = {
    '|': ['N', 'S'],
    '-': ['E', 'W'],
    'F': ['S', 'E'],
    '7': ['S', 'W'],
    'J': ['N', 'W'],
    'L': ['N', 'E']
}

grid = []
width = 0
height = 0

def PrintGrid(grid):
    for row in grid:
        for cell in row:
            print(cell, end='')
        print()
    print()

def GetAdjacent(dirs, x, y):
    out = []
    for d in dirs:
        if d == 'N' and y > 0:
            out.append((x, y-1, grid[y-1][x]))
        elif d == 'NE' and y > 0 and x < (width-1):
            out.append((x+1, y-1, grid[y-1][x+1]))
        elif d =='E' and x < (width-1):
            out.append((x+1, y, grid[y][x+1]))
        elif d =='SE' and y < (height-1) and x < (width-1):
            out.append((x+1, y+1, grid[y+1][x+1]))
        elif d == 'S' and y < (height-1):
            out.append((x, y+1, grid[y+1][x]))
        elif d == 'SW' and y < (height-1) and x > 0:
            out.append((x-1, y+1, grid[y+1][x-1]))
        elif d == 'W' and x > 0:
            out.append((x-1, y, grid[y][x-1]))
        elif d == 'NW' and y > 0 and x > 0:
            out.append((x-1, y-1, grid[y-1][x-1]))
    return out

def PopulateInput(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        global width
        global height
        width = len(lines[0])
        height = len(lines)
        global grid
        for y, row in enumerate(lines):
            grid.append([])
            for x, cell in enumerate(row):
                grid[y].append(cell)

def GenerateLoop(startType):
    # 1. Find the start position and populate grid
    vertices = []
    startPos = None
    # global grid
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == 'S':
                startPos = (x, y, startType)
                grid[y][x] = startType
                print(f'S at x={x}, y={y}')

    if startType in ['L', 'J', '7', 'F']:
        vertices.append((startPos[0], startPos[1]))

    # 2. Now we can just traverse the loop until we get back to startPos,
    #    then divide by 2
    loop = [startPos]
    # currentPos = GetAdjacent(['S'], startPos[0], startPos[1])[0]
    currentPos = startPos
    # history.append(currentPos)
    # print(f'Moved to {currentPos}')
    count = 1
    # while currentPos != startPos and len(history) > 1:
    while True:
        posList = GetAdjacent(directions[currentPos[2]], currentPos[0], currentPos[1])
        # print(posList)
        revised = [p for p in posList if p not in loop]
        if len(revised) > 0:
            currentPos = revised[0]
            loop.append(currentPos)
            count += 1
            if grid[currentPos[1]][currentPos[0]] in ['L', 'J', '7', 'F']:
                vertices.append((currentPos[0], currentPos[1]))
        else:
            break # done
        # print(f'Moved to {currentPos}\n')
        if count % 100 == 0: print(f'Done {count}')
    return loop, vertices

def Determinant(v1, v2):
    d = (v1[0]*v2[1]) - (v1[1]*v2[0])
    # print(f'Determinant of {v1} and {v2} is {d}')
    return d

def Area(vertices):
    result = 0
    for i in range(len(vertices)):
        # print(f'i={i}')
        # print(f'(i+1)%len(vertices)={(i+1)%len(vertices)}')
        result += Determinant(vertices[i], vertices[(i+1)%len(vertices)])
    # print(result)
    result /= 2
    # print(result)
    return result    

def Day10(filename, startType):
    PopulateInput(filename)
    loop, vertices = GenerateLoop(startType)
    perimeter = len(loop)
    print(f'Size of loop = {perimeter}')
    print(f'Furthest position = {perimeter/2}')

    # # Part 2
    # print()
    # PrintGrid(grid)
    # for v in vertices:
    #     print(v)

    area = abs(Area(vertices))
    print(f'Area = {area}')
    print(f'Enclosed Tiles = {area - (perimeter/2) + 1}')

# Day10('test.txt', 'F')
# Day10('test_1.txt', 'F')
# Day10('test_2.txt', 'F')
# Day10('test_3.txt', 'F')
# Day10('test_4.txt', '7')
Day10('input.txt', '|')

