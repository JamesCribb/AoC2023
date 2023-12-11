def Day11(expansion):
    lines = []
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    
    grid = []
    for line in lines:
        grid.append([])
        for c in line:
            grid[-1].append(c)

    # Identify empty rows and cols
    emptyRows = []
    for y in range(len(grid)):
        if '#' not in grid[y]:
            emptyRows.append(y)
    emptyCols = []
    for x in range(len(grid)):
        hasGalaxy = False
        for y in range(len(grid)):
            if grid[y][x] == '#':
                hasGalaxy = True
                break
        if hasGalaxy == False:
            emptyCols.append(x)
    # print(f'Empty rows: {emptyRows}')
    # print(f'Empty cols: {emptyCols}')

    galaxies = []
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if grid[y][x] == '#':
                galaxies.append((len(galaxies)+1, x, y))
    # for g in galaxies:
    #     print(g)
    # print(f'Num galaxies: {len(galaxies)}')
   
    pairs = []
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            pairs.append((i+1, j+1))
    # for pair in pairs:
    #     print(pair)
    # print(f'Num pairs = {len(pairs)}')

    result = 0
    for pair in pairs:
        g1 = galaxies[pair[0]-1]
        g2 = galaxies[pair[1]-1]

        distance = abs(g2[1] - g1[1]) + abs(g2[2] - g1[2])
        for er in emptyRows:
            if min(g1[2], g2[2]) < er < max(g1[2], g2[2]):
                distance += expansion
        for ec in emptyCols:
            if min(g1[1], g2[1]) < ec < max(g1[1], g2[1]):
                distance += expansion

        # print(f'Distance between galaxies {g1[0]} and {g2[0]} is {distance}')
        result += distance
    print(f'Result={result}')

part1 = 1
part2 = 999999
Day11(part2)