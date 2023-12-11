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

def Part1():
    with open('input.txt', 'r') as f:
        global grid
        lines = [line.strip() for line in f.readlines()]
        global width
        global height
        width = len(lines[0])
        height = len(lines)
    # 1. Find the start position and populate grid
    startPos = None
    for y, row in enumerate(lines):
        grid.append([])
        for x, c in enumerate(row):
            if lines[y][x] == 'S':
                startPos = (x, y, '|')
                grid[y].append('|') # by inspection...
                print(f'S at x={x}, y={y}')
            else:
                grid[y].append(lines[y][x])
    # 2. Now we can just traverse the loop until we get back to startPos,
    #    then divide by 2
    history = [startPos]
    # currentPos = GetAdjacent(['S'], startPos[0], startPos[1])[0]
    currentPos = startPos
    # history.append(currentPos)
    # print(f'Moved to {currentPos}')
    count = 1
    # while currentPos != startPos and len(history) > 1:
    while True:
        posList = GetAdjacent(directions[currentPos[2]], currentPos[0], currentPos[1])
        # print(posList)
        revised = [p for p in posList if p not in history]
        if len(revised) > 0:
            currentPos = revised[0]
            history.append(currentPos)
            count += 1
        else:
            break # done
        # print(f'Moved to {currentPos}\n')
        if count % 100 == 0: print(f'Done {count}')
    print(f'Size of loop: {count}')
    print(f'Farthest point = {count//2}')
    
    # Save for processing in part 2
    with open('vertices.txt', 'w') as outFile:
        for v in history:
            outFile.write(f'{v[0]} {v[1]} {v[2]}\n')
    print('Done')
    
# Part1()

def Determinant(v1, v2):
    d = (v1[0]*v2[1]) - (v1[1]*v2[0])
    print(f'Determinant of {v1} and {v2} is {d}')
    return d

def Area(vertices):
    result = 0
    for i in range(len(vertices)):
        print(f'i={i}')
        print(f'(i+1)%len(vertices)={(i+1)%len(vertices)}')
        result += Determinant(vertices[i], vertices[(i+1)%len(vertices)])
    print(result)
    result /= 2
    print(result)
    return result

def Part2():
    lines = []
    vertices = []
    with open('vertices.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        for line in lines:
            toks = line.split(' ')
            if toks[2] in ['F', 'L', 'J', '7']:
                vertices.append((int(toks[0]), int(toks[1]), toks[2]))
    
    print(len(vertices))
    
    
Part2()