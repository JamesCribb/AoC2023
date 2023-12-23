import sys
sys.path.append('../Utils')

from Grid import *

def GetInput(fname):
    lines = []
    with open(fname, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    grid = Grid(lines)
    return grid

def Day21(fname):
    grid = GetInput(fname)
    print(grid)

    start = grid.Find('S')
    grid.grid[start[1]][start[0]] = '.'

    positions = {(start[0], start[1])}
    numSteps = 64
    for i in range(numSteps):
        newPositions = set()
        for pos in positions:
            adjacent = grid.NESW(pos[0], pos[1])
            for adj in adjacent:
                if adj[2] != '#':
                    newPositions.add((adj[0], adj[1]))
        positions = newPositions
        print(f'{len(positions)} positions after {i+1} steps')

    print(grid.width*grid.height)

Day21('input.txt')