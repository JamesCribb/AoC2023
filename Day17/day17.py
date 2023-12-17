import math

# A node represents an XY position in the grid, plus every possible state in which
# we can arrive at the node: direction {N, E, S, W} plus number of prior steps in that direction
# {1, 2, 3}. This will affect what the node's neighbours are. 
class Node:
    def __init__(self, id, grid):
        toks = id.split('-')
        self.x = int(toks[0])
        self.y = int(toks[1])
        self.dir = toks[2]
        self.n = int(toks[3])
        self.neighbours = []
        self.cost = grid[self.y][self.x]
        self.distance = math.inf
    def Id(self):
        return f'{self.x}-{self.y}-{self.dir}-{self.n}'

def GetInput(filename):
    grid = []
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        for line in lines:
            grid.append([])
            for c in line:
                grid[-1].append(int(c))
    return grid

# A node may have up to 4 neighbours: 1 each to the north, east, south and west
# A neighbour exists iff:
# 1. The neighbour's XY position is within the grid
# 2. The direction from the node to the neighbour is not the opposite of the direction
#    to the current node (ie a node with dir=N cannot have a neighbour with dir=S)
# 3. If the neighbour's direction is the same as the node's direction, it cannot exceed
#    the maximum steps allowable in that direction
def GetNeighbours_1(id, grid, graph, maxSteps):
    width = len(grid[0])
    height = len(grid)
    neighbours = []
    node = graph[id]
    # North
    if (node.y > 0) and (node.dir != 'S') and ((node.dir != 'N') or (node.n < maxSteps)):
        neighbours.append(f'{node.x}-{node.y-1}-{"N"}-{1 if node.dir != "N" else node.n + 1}')
    # East
    if (node.x < (width-1)) and (node.dir != 'W') and ((node.dir != 'E') or (node.n < maxSteps)):
        neighbours.append(f'{node.x+1}-{node.y}-{"E"}-{1 if node.dir != "E" else node.n + 1}')
    # South
    if (node.y < (height-1)) and (node.dir != 'N') and ((node.dir != 'S') or (node.n < maxSteps)):
        neighbours.append(f'{node.x}-{node.y+1}-{"S"}-{1 if node.dir != "S" else node.n + 1}')
    # West
    if (node.x > 0) and (node.dir != 'E') and ((node.dir != 'W') or (node.n < maxSteps)):
        neighbours.append(f'{node.x-1}-{node.y}-{"W"}-{1 if node.dir != "W" else node.n + 1}')
    return neighbours

# Similar to the above, but with modified rules:
# 1. The neighbour's XY position must be within the grid
# 2. The direction from the node to the neighbour must not be the opposite of the direction of
#    the current node
# 3. If the neighbour's direction is the same as the node's direction, it cannot exceed the 
#    maximum steps allowable in that direction
# 4. If the crucible has started moving, it must move a minimum number of steps before turning
def GetNeighbours_2(id, grid, graph, minSteps, maxSteps):
    width = len(grid[0])
    height = len(grid)
    neighbours = []
    node = graph[id] 
    # North
    if ((node.y > 0) 
        and (node.dir != 'S') 
        and ((node.n == 0) or 
            ((node.dir == 'N' and node.n < maxSteps) or (node.dir != 'N' and node.n >= minSteps)))):
        neighbours.append(f'{node.x}-{node.y-1}-{"N"}-{1 if node.dir != "N" else node.n + 1}')
    # East
    if ((node.x < (width-1)) 
        and (node.dir != 'W') 
        and ((node.n == 0) or 
            ((node.dir == 'E' and node.n < maxSteps) or (node.dir != 'E' and node.n >= minSteps)))):
        neighbours.append(f'{node.x+1}-{node.y}-{"E"}-{1 if node.dir != "E" else node.n + 1}')
    # South
    if ((node.y < (height-1)) 
        and (node.dir != 'N') 
        and ((node.n == 0) or
            ((node.dir == 'S' and node.n < maxSteps) or (node.dir != 'S' and node.n >= minSteps)))):
        neighbours.append(f'{node.x}-{node.y+1}-{"S"}-{1 if node.dir != "S" else node.n + 1}')
    # West
    if ((node.x > 0) 
        and (node.dir != 'E') 
        and ((node.n == 0) or
            ((node.dir == 'W' and node.n < maxSteps) or (node.dir != 'W' and node.n >= minSteps)))):
        neighbours.append(f'{node.x-1}-{node.y}-{"W"}-{1 if node.dir != "W" else node.n + 1}')
    return neighbours

def BuildGraph(grid, minSteps, maxSteps):
    graph = {}
    # Start with the start node, which has no direction (X)
    pendingNodes = ['0-0-X-0']
    while len(pendingNodes) > 0:
        # print(f'Pending nodes: {pendingNodes}')
        # input()
        nodeId = pendingNodes[0]
        if nodeId not in graph:
            graph[nodeId] = Node(nodeId, grid)
            if len(graph) % 1000 == 0:
                print(f'Graph size: {len(graph)}...')
            # neighbours = GetNeighbours_1(nodeId, grid, graph, maxSteps)
            neighbours = GetNeighbours_2(nodeId, grid, graph, minSteps, maxSteps)
            graph[nodeId].neighbours = neighbours
            for n in neighbours:
                pendingNodes.append(n)
        pendingNodes = pendingNodes[1:] # Remove the node we just examined

    return graph

def Day17():
    grid = GetInput('input.txt')

    # Transform the grid into a state where it can be solved with Dijkstra's algorithm
    # graph = BuildGraph(grid, 3)
    graph = BuildGraph(grid, 4, 10)
    print(f'Total graph size: {len(graph)}')

    # Get the target position
    targetX = len(grid[0]) - 1
    targetY = len(grid) - 1
    # Get all possible target IDs
    dirs = ['N', 'E', 'S', 'W']
    # steps = [1, 2, 3]
    steps = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    targetIds = []
    for dir in dirs:
        for step in steps:
            targetId = f'{targetX}-{targetY}-{dir}-{step}'
            if targetId in graph: # not guaranteed that each possible end location is reachable
                targetIds.append(targetId)
            else:
                print(f'Target {targetId} not in graph')
    print('Target IDs:')
    for targetId in targetIds:
        print(targetId)

    debugCounter = 0
    touchedIds = set() # Holds IDs of nodes that have been assigned a tentative distance

    graph['0-0-X-0'].distance = 0
    currentNodeId = '0-0-X-0'
    results = {}
    while True:
        currentNode = graph[currentNodeId]
        # print(f'Examining {currentNodeId}')
        # print(f'Neighbours: {currentNode.neighbours}')
        for neighbourId in currentNode.neighbours:
            if neighbourId in graph:
                neighbourNode = graph[neighbourId]
                distance = min(neighbourNode.distance, currentNode.distance + neighbourNode.cost)
                graph[neighbourId].distance = distance
                touchedIds.add(neighbourId)
        debugCounter += 1
        if debugCounter % 1000 == 0:
            print(f'Found shortest path to {debugCounter} nodes!')
        if currentNodeId in targetIds:
            assert currentNodeId not in results
            results[currentNodeId] = currentNode.distance
            print('***** Found shortest path to an end node !!! *****')
            if len(results) == len(targetIds):
                break
        # Remove the currentNode from the graph - should speed things up
        graph.pop(currentNodeId)
        if currentNodeId in touchedIds:
            touchedIds.remove(currentNodeId)
        # Get the next node
        nextNodeId = ''
        nextDistance = math.inf
        for nodeId in touchedIds:
            node = graph[nodeId]
            if node.distance < nextDistance:
                nextDistance = node.distance
                nextNodeId = nodeId
        currentNodeId = nextNodeId

    for k, v in results.items():
        print(f'Node {k}: {v}')

Day17()