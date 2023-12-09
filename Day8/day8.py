class Node:
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right

nodes = {}
steps = []

def GetInput(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        global steps
        steps = lines[0]
        for i in range(2, len(lines)):
            name = lines[i].split(' ')[0]
            left = lines[i].split(',')[0][-3:]
            right = lines[i].split(',')[1][1:4]
            nodes[name] = Node(name, left, right)        

def GetSteps(startName, endName):
    nodeSteps = {}
    currentNode = nodes[startName]
    stepCount = 0
    while currentNode.name != endName:
        modStepCount = stepCount % len(steps)
        step = steps[modStepCount]
        if step == 'L':
            currentNode = nodes[currentNode.left]
        elif step == 'R':
            currentNode = nodes[currentNode.right]
        # If we've already visited this node at the current step,
        # then our destination node is unreachable
        if currentNode.name in nodeSteps.keys():
            if modStepCount in nodeSteps[currentNode.name]:
                print(f'Node {endName} is never reachable from {startName}')
                return -1
            else: 
                nodeSteps[currentNode.name].append(modStepCount)
        else:
            nodeSteps[currentNode.name] = [modStepCount]
        # print(nodeSteps)
        # input()
        stepCount += 1
    return stepCount

def Part1():
    GetInput('input.txt')
    startName = 'AAA'
    endName = 'ZZZ'
    stepCount = GetSteps(startName, endName)
    print(f'Took {stepCount} steps to reach ZZZ')

def Part2_BF():
    GetInput('input.txt')
    currentNodes = [sn for sn in nodes.values() if sn.name[-1] == 'A']
    endNodes = [en for en in nodes.keys() if en[-1] == 'Z']
    stepCount = 0
    allAtEnd = False
    # print([cn.name for cn in currentNodes])
    while allAtEnd == False:
        step = steps[stepCount % len(steps)]
        # print(f'step={step}')
        for i, cn in enumerate(currentNodes):
            if step == 'L':
                currentNodes[i] = nodes[cn.left]
            elif step == 'R':
                currentNodes[i] = nodes[cn.right]
        # print([cn.name for cn in currentNodes])
        stepCount += 1
        allAtEnd = True
        for cn in currentNodes:
            if cn.name not in endNodes:
                allAtEnd = False         
        if stepCount % 100000 == 0:
            print(f'Done {stepCount} steps...')
    print(f'stepCount={stepCount}')

def GCD(a, b):
    assert a >= 0 and b >= 0
    if a == b: return b
    if a < b:
        temp = a
        a = b
        b = temp
    r = a % b
    if r == 0: return b
    else: return GCD(b, r)

def LCM(a, b):
    return abs(a*b) / (GCD(a, b))

def Part2():
    GetInput('input.txt')
    # There are only 6 nodes each ending with A and Z
    # Begin by storing the number of steps required to reach each Z from each A
    # (or -1 if unreachable)
    stepsToNodes = {}
    for startNode in nodes.values():
        if startNode.name[-1] == 'A':
            stepsToNodes[startNode.name] = {}
            for endNode in nodes.values():
                if endNode.name[-1] == 'Z':
                    print(f'Getting steps from {startNode.name} to {endNode.name}')
                    steps = GetSteps(startNode.name, endNode.name)
                    print(f'Steps={steps}')
                    stepsToNodes[startNode.name][endNode.name] = steps
    # for stn in stepsToNodes.keys():
    #     print(stn)
    #     for endNode, steps in stepsToNodes[stn].items():
    #         print(f'\t{endNode}: {steps}')

    # It turns out that each startNode can only reach one end node
    # So all we have to do now is find the least common multiple for each result
    # NOTE: It turns out this only works because the number of steps from **Z back to **Z will 
    #       always equal the number of steps from **A to **Z. 
    results = []
    for stepsByStartNode in stepsToNodes.values():
        for steps in stepsByStartNode.values():
            if steps != -1:
                results.append(steps)
    print(results)
    answer = LCM(results[0], results[1])
    for i in range(2, len(results)):
        answer = LCM(answer, results[i])

    print(f'Answer: {answer}')

# Part1()
Part2()
# Part2_BF()