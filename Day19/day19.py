class Condition:
    def __init__(self, partType, fn, comp, result):
        self.partType = partType
        self.minVal = (comp + 1) if fn == '>' else 1
        self.maxVal = (comp - 1) if fn == '<' else 4000
        self.result = result
    def Check(self, part):
        return self.minVal <= part[self.partType] <= self.maxVal
    def __str__(self):
        return f'Type={self.partType} Min={self.minVal} Max={self.maxVal} : {self.result}'

class Workflow:
    def __init__(self):
        self.conditions = []
        self.terminator = None
    def __str__(self):
        s = f'Conditions:\n'
        for c in self.conditions:
            s += f'\t{c}\n'
        s += f'Terminator: {self.terminator}\n'
        return s

def GetInput(filename):
    workflows = {}
    parts = []
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        idx = 0

        # Parse workflow
        for i, line in enumerate(lines):
            if line == '':
                idx = i + 1
                break
            wfId = line.split('{')[0]
            wfData = line.split('{')[1][:-1].split(',')
            wf = Workflow()
            for j in range(len(wfData)-1):
                conditionData = wfData[j]
                partVal = conditionData[0]
                fn = conditionData[1]
                compVal = int(conditionData[2:conditionData.find(':')])
                result = conditionData[conditionData.find(':')+1:]
                condition = Condition(partVal, fn, compVal, result)
                wf.conditions.append(condition)
            wf.terminator = wfData[-1]
            workflows[wfId] = wf

        # Parse parts
        for i in range(idx, len(lines)):
            partData = lines[i].split(',')
            # print(partData)
            x = int(partData[0][3:])
            m = int(partData[1][2:])
            a = int(partData[2][2:])
            s = int(partData[3][2:-1])
            parts.append({'x': x, 'm': m, 'a': a, 's': s})

    return workflows, parts

def GetValidRanges(workflows, currentRange, partState, conditionIdx, endRanges):
    print(f'Current Range: {currentRange}\nPart State: {partState} Condition Idx: {conditionIdx}')
    if partState == 'A':
        print(f'***** Found a valid end range: {currentRange} *****')
        endRanges.append(currentRange)
        return
    elif partState == 'R':
        print(f'Discarding an end range: {currentRange}')
        return
    else:
        wf = workflows[partState]
        assert conditionIdx < len(wf.conditions)
        condition = wf.conditions[conditionIdx]
        partType = condition.partType
        partRange = currentRange[partType]
        print(f'Condition: {condition}')
        print(f'Part range: {partRange}')
        validRange = [max(partRange[0], condition.minVal), min(partRange[1], condition.maxVal)]
        invalidRange = []
        if validRange[0] > validRange[1]:
            validRange = []
            invalidRange = [partRange.copy()]
        elif validRange[0] > partRange[0]:
            invalidRange = [partRange[0], validRange[0]-1]
        elif validRange[1] < partRange[1]:
            invalidRange = [validRange[1]+1, partRange[1]]
        print(f'Valid range: {validRange}')
        print(f'Invalid range: {invalidRange}')
        print()
        # input()
        if len(validRange) == 2:
            newValidRange = currentRange.copy()
            newValidRange[partType] = validRange
            newPartState = condition.result
            GetValidRanges(workflows, newValidRange, newPartState, 0, endRanges)
        if len(invalidRange) == 2:
            newInvalidRange = currentRange.copy()
            newInvalidRange[partType] = invalidRange
            conditionIdx += 1
            if conditionIdx < len(wf.conditions):
                GetValidRanges(workflows, newInvalidRange, partState, conditionIdx, endRanges)
            else:
                GetValidRanges(workflows, newInvalidRange, wf.terminator, 0, endRanges)

def Part1():
    workflows, parts = GetInput('input.txt')
    total = 0
    for part in parts:
        partState = 'in'
        while partState not in ['A', 'R']:
            wf = workflows[partState]
            passed = False
            for cond in wf.conditions:
                if cond.Check(part) == True:
                    partState = cond.result
                    passed = True
                    break
            if passed == False:
                partState = wf.terminator
        if partState == 'A':
            total += sum(part.values())
    print(f'Total={total}')

def Part2():
    workflows, _ = GetInput('input.txt')
    validRanges = []
    startRange = {'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000]}
    GetValidRanges(workflows, startRange, 'in', 0, validRanges)

    for vr in validRanges:
        print(vr)
    print(len(validRanges))

    # Because we have a single entry point, we are guaranteed to have no overlaps in the valid
    # ranges. 
    total = 0
    for vr in validRanges:
        rangeTotal = 0
        for partRange in vr.values():
            partTotal = partRange[1] - partRange[0] + 1
            if rangeTotal == 0:
                rangeTotal = partTotal
            else:
                rangeTotal *= partTotal
        total += rangeTotal

    print(f'Result = {total}')

def Day19():
    # Part1()
    Part2()

Day19()