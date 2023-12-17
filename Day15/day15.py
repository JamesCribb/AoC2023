import re

def Hash(s):
    result = 0
    for c in s:
        result += ord(c)
        result *= 17
        result %= 256
    return result

def Day15():
    sequence = []
    with open('input.txt', 'r') as f:
        line = f.readline()
        sequence = line.split(',')
    
    boxes = []
    for _ in range(256):
        boxes.append([])

    for step in sequence:
        splitIdx = re.search(r'[=-]', step).start()
        label = step[:splitIdx]
        boxIdx = Hash(label)
        op = step[splitIdx:]
        if op[0] == '-':
            for i in range(len(boxes[boxIdx])):
                if boxes[boxIdx][i][0] == label:
                    if i == len(boxes) - 1:
                        boxes[boxIdx] = boxes[boxIdx][:i]
                    else: 
                        boxes[boxIdx] = boxes[boxIdx][:i] + boxes[boxIdx][i+1:]
                    break
        elif op[0] == '=':
            focalLength = int(op[1:])
            match = False
            for i in range(len(boxes[boxIdx])):
                if boxes[boxIdx][i][0] == label:
                    boxes[boxIdx][i] = (label, focalLength)
                    match = True
            if match == False:
                boxes[boxIdx].append((label, focalLength))
        # # DEBUG
        # print(f'After {step}:')
        # for i, box in enumerate(boxes):
        #     if len(box) > 0:
        #         print(f'Box {i}: {box}')
        # print()

    # Calculate focusing power
    totalPower = 0
    for i, box in enumerate(boxes):
        for j, lens in enumerate(box):
            focusingPower = (i + 1) * (j + 1) * (lens[1])
            totalPower += focusingPower
    print(f'Total focusing power: {totalPower}')

    # Part 1
    # result = 0
    # for s in sequence:
    #     result += Hash(s)
    # print(result)



Day15()