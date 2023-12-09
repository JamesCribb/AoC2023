digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def ParseNum(grid, parsedLocations, x, y):
    print(f'Starting at x={x}, y={y}. Val={grid[y][x]}')
    parsedLocations.append((y, x))
    numString = grid[y][x]
    # Check to the right
    rPos = x + 1
    while rPos < len(grid[0]) and grid[y][rPos] in digits:
        # num = (num * 10) + int(grid[y][rPos])
        numString += grid[y][rPos]
        parsedLocations.append((y, rPos))
        rPos += 1
    # Check to the left
    lPos = x - 1
    while lPos > -1 and grid[y][lPos] in digits:
        # num += int(grid[y][lPos]) * (10**len(numStr))
        numString = grid[y][lPos] + numString
        parsedLocations.append((y, lPos))
        lPos -= 1
    num = int(numString)
    print(f'Parsed {num}')
    return num

def Part2():
    with open('input.txt', 'r') as f:
        grid = [line.strip() for line in f.readlines()]
        
        height = len(grid)
        width = len(grid[0])

        sum = 0

        for y, row in enumerate(grid):
            for x, c in enumerate(row):
                if c not in digits and c == '*':

                    # We only care about duplications within gears
                    parsedLocations = []
                    parts = []
                    gearRatio = 0

                    # Search for adjacent, unparsed numbers
                    # N
                    if y > 0 and grid[y-1][x] in digits and (y-1, x) not in parsedLocations:
                        parts.append(ParseNum(grid, parsedLocations, x, y-1))
                    # NE
                    if y > 0 and x < width-1 and grid[y-1][x+1] in digits and (y-1, x+1) not in parsedLocations:
                        parts.append(ParseNum(grid, parsedLocations, x+1, y-1))
                    # E
                    if x < width-1 and grid[y][x+1] in digits and (y, x+1) not in parsedLocations:
                        parts.append(ParseNum(grid, parsedLocations, x+1, y))
                    # SE
                    if y < height-1 and x < width-1 and grid[y+1][x+1] in digits and (y+1, x+1) not in parsedLocations:
                        parts.append(ParseNum(grid, parsedLocations, x+1, y+1))
                    # S
                    if y < height-1 and grid[y+1][x] in digits and (y+1, x) not in parsedLocations:
                        parts.append(ParseNum(grid, parsedLocations, x, y+1))
                    # SW
                    if y < height-1 and x > 0 and grid[y+1][x-1] in digits and (y+1, x-1) not in parsedLocations:
                        parts.append(ParseNum(grid, parsedLocations, x-1, y+1))
                    # W
                    if x > 0 and grid[y][x-1] in digits and (y, x-1) not in parsedLocations:
                        parts.append(ParseNum(grid, parsedLocations, x-1, y))
                    # NW
                    if y > 0 and x > 0 and grid[y-1][x-1] in digits and (y-1, x-1) not in parsedLocations:
                        parts.append(ParseNum(grid, parsedLocations, x-1, y-1)) 

                    if len(parts) == 2:
                        gearRatio = parts[0] * parts[1]
                        sum += gearRatio

        print(f'Sum={sum}')


Part2()