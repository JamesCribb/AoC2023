import sys

NORTH = (0, -1)
EAST  = (1, 0)
SOUTH = (0, 1)
WEST  = (-1, 0)

def InsideGrid(beamPos, grid):
    return (0 <= beamPos[0] < len(grid[0])) and (0 <= beamPos[1] < len(grid))

def GetInput(filename):
    grid = []
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        for line in lines:
            grid.append(line)
    return grid

def PrintGrid(grid):
    for row in grid:
        for cell in row:
            print(cell, end='')
        print()

def PlotBeam(grid, beamPos, beamDir, beamPath, pathSet):
    # print()
    # print(f'PlotBeam pos={beamPos} dir={beamDir} path={beamPath} done={beamPaths}')

    # Update beam position based on current position and direction
    newPos = (beamPos[0] + beamDir[0], beamPos[1] + beamDir[1])
    # print(f'NewPos={newPos}')

    if InsideGrid(newPos, grid) == True:
        if (newPos, beamDir) not in pathSet:
            if (newPos, beamDir) not in beamPath:
                beamPath.append((newPos, beamDir))
                # Update the beam direction and/or split the beam, based on the grid value
                c = grid[newPos[1]][newPos[0]]
                # print(f'Grid value = {c}')
                if c == '.':
                    PlotBeam(grid, newPos, beamDir, beamPath, pathSet) # no change
                elif c == '/':
                    if beamDir == NORTH: beamDir = EAST
                    elif beamDir == EAST: beamDir = NORTH
                    elif beamDir == SOUTH: beamDir = WEST
                    elif beamDir == WEST: beamDir = SOUTH
                    PlotBeam(grid, newPos, beamDir, beamPath, pathSet)
                elif c == '\\':
                    if beamDir == NORTH: beamDir = WEST
                    elif beamDir == EAST: beamDir = SOUTH
                    elif beamDir == SOUTH: beamDir = EAST
                    elif beamDir == WEST: beamDir = NORTH
                    PlotBeam(grid, newPos, beamDir, beamPath, pathSet)            
                elif c == '-':
                    if (beamDir == EAST) or (beamDir == WEST):
                        PlotBeam(grid, newPos, beamDir, beamPath, pathSet)
                    elif (beamDir == NORTH) or (beamDir == SOUTH):
                        PlotBeam(grid, newPos, EAST, beamPath.copy(), pathSet)
                        PlotBeam(grid, newPos, WEST, beamPath.copy(), pathSet)
                elif c == '|':
                    if (beamDir == NORTH) or (beamDir == SOUTH):
                        PlotBeam(grid, newPos, beamDir, beamPath, pathSet)
                    elif (beamDir == EAST) or (beamDir == WEST):
                        PlotBeam(grid, newPos, NORTH, beamPath.copy(), pathSet)
                        PlotBeam(grid, newPos, SOUTH, beamPath.copy(), pathSet)
            else:
                # If we have an infinite loop in our current path, terminate
                for bp in beamPath:
                    pathSet.add(bp)
                # print(f'Added a path. New length: {len(pathSet)}')
        else:
            # If the new position/direction is already in the pathset, then we've already calculated
            # an equivalent path for a different branch
            for bp in beamPath:
                pathSet.add(bp)
            # print(f'Added a path. New length: {len(pathSet)}')
    else:
        # If the new position is outside the grid, this branch is finished
        for bp in beamPath:
            pathSet.add(bp)
        # print(f'Added a path. New length: {len(pathSet)}')

def EnergisedTiles(grid, beamPos, beamDir):
    pathSet = set()
    PlotBeam(grid, beamPos, beamDir, [], pathSet)
    uniqueTiles = set()
    for p in pathSet:
        uniqueTiles.add(p[0])
    return len(uniqueTiles)

def Day16():
    grid = GetInput('input.txt')
    sys.setrecursionlimit(10000) # Not great, I could have used more iteration...

    # # Part 1
    # energisedTiles = EnergisedTiles(grid, (-1, 0), EAST)
    # print(f'Energised Tiles: {energisedTiles}')

    # Part 2
    width = len(grid[0])
    height = len(grid)
    energisedTiles = []
    # Check each beam direction from each edge tile
    # NORTH
    for x in range(width):
        energisedTiles.append(EnergisedTiles(grid, (x, height), NORTH))
        print(f'Done {x+1} of {width}')
    print(f'Done North')
    # EAST
    for y in range(height):
        energisedTiles.append(EnergisedTiles(grid, (-1, y), EAST))
        print(f'Done {y+1} of {height}')
    print(f'Done East')
    # SOUTH
    for x in range(width):
        energisedTiles.append(EnergisedTiles(grid, (x, -1), SOUTH))
        print(f'Done {x+1} of {width}')
    print(f'Done South')
    # WEST
    for y in range(height):
        energisedTiles.append(EnergisedTiles(grid, (width, y), WEST))
        print(f'Done {y+1} of {height}')
    print(f'Done West')
    print(f'Best result: {max(energisedTiles)}')

if __name__ == '__main__':
    Day16()
