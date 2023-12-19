
# def Determinant(v1, v2):
#     return (v1[0] * v2[1]) - (v1[1] * v2[0])

import collections
import math

def PrintGrid(grid):
    for row in grid:
        for cell in row:
            print(cell, end='')
        print()

def GetUnfilledNeighbours(grid, cell):
    neighbours = []
    x = cell[0]
    y = cell[1]
    width = len(grid[0])
    height = len(grid)
    # N
    if y > 0:
        neighbours.append((x, y-1))
    # NE
    if (x < (width - 1)) and (y > 0):
        neighbours.append((x+1, y-1))
    # E
    if x < (width-1):
        neighbours.append((x+1, y))
    # SE
    if (x < (width - 1)) and (y < (height - 1)):
        neighbours.append((x+1, y+1))
    # S
    if y < (height - 1):
        neighbours.append((x, y+1))
    # SW
    if (x > 0) and (y < (height - 1)):
        neighbours.append((x-1, y+1))
    # W
    if x > 0:
        neighbours.append((x-1, y))
    # NW
    if (x > 0) and (y > 0):
        neighbours.append((x-1, y-1))
    unfilledNeighbours = [cell for cell in neighbours if grid[cell[1]][cell[0]] not in ['O', '#']]
    return unfilledNeighbours

def Day18():
    
    instructions = []
    
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        for line in lines:
            toks = line.split(' ')
            dir = toks[0]
            length = int(toks[1])
            colour = toks[2] # unused so far...
            instructions.append((dir, length, colour))
    
    vertices = [(0, 0)]
    for instr in instructions:
        dir = instr[0]
        length = instr[1]
        offset = None
        if dir == 'U':
            offset = (0, -length)
        elif dir == 'R':
            offset = (length, 0)
        elif dir == 'D':
            offset = (0, length)
        elif dir == 'L':
            offset = (-length, 0)
        lastVertex = vertices[-1]
        nextVertex = (lastVertex[0] + offset[0], lastVertex[1] + offset[1])
        vertices.append(nextVertex)

    # for v in vertices:
    #     print(v)

    # area = 0
    # for i in range(len(vertices)):
    #     det = Determinant(vertices[i], vertices[(i + 1) % len(vertices)])
    #     print(f'Determinant of {vertices[i]} and {vertices[(i + 1) % len(vertices)]} = {det}')
    #     area += det
    # area /= 2
    # print(f'Area = {area}')

    minX = math.inf
    minY = math.inf
    maxX = -math.inf
    maxY = -math.inf
    for v in vertices:
        minX = min(minX, v[0])
        minY = min(minY, v[1])
        maxX = max(maxX, v[0])
        maxY = max(maxY, v[1])
    print(f'minX = {minX}, minY = {minY}')
    print(f'maxX = {maxX}, maxY = {maxY}')
    # Transform vertices so that min(x) = 1 and min(y) = 1
    for i, v in enumerate(vertices):
        vertices[i] = (v[0] - (minX-1)), (v[1] - (minY-1))
    # Also transform maximums
    maxX -= minX
    maxY -= minY

    grid = []
    for _ in range(maxY+3):
        grid.append([])
        for _ in range(maxX+3):
            grid[-1].append('.')

    # Mark edges
    for i in range(len(vertices)-1):
        v1 = vertices[i]
        v2 = vertices[i+1]
        for x in range(min(v1[0], v2[0]), max(v1[0], v2[0])+1):
            grid[v1[1]][x] = '#'
        for y in range(min(v1[1], v2[1]), max(v1[1], v2[1])+1):
            grid[y][v1[0]] = '#'
    
    print(f'Grid = {len(grid[0])} * {len(grid)}')
    # PrintGrid(grid)

    # Starting from the top-left, mark all empty spaces
    count = 0
    unfilled = set()
    unfilled.add((0, 0))
    marked = set() # DEBUG
    while len(unfilled) > 0:
        cell = unfilled.pop()
        grid[cell[1]][cell[0]] = 'O'
        if cell in marked:
            print(f'Cell: {cell}')
            assert False
        marked.add(cell)
        # print(f'Checked {cell}')
        for neighbour in GetUnfilledNeighbours(grid, cell):
            unfilled.add(neighbour)
        count += 1
        if count % 1000 == 0:
            print(f'Marked {count} unfilled spaces')

    # PrintGrid(grid)

    filledArea = len(grid[0]) * len(grid)
    for row in grid:
        for cell in row:
            if cell == 'O':
                filledArea -= 1

    print(f'Filled area: {filledArea}')

    # # Count filled area
    # count = 0
    # for y, row in enumerate(grid):
    #     for x, c in enumerate(row):
    #         if c == '#': count += 1
    #         else:
    #             ins
    #             for cy in range(y, -1, -1):
    #                 if grid[cy][x] == '#':


Day18()