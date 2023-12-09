import math

def Part1():
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        sum = 0
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        for line in lines:
            firstDigit = None
            lastDigit = None
            for i in range(0, len(line)):
                if line[i] in digits:
                    firstDigit = int(line[i])
                    break
            for i in range(-1, -len(line) - 1, -1):
                if line[i] in digits:
                    lastDigit = int(line[i])
                    break
            sum += (firstDigit * 10) + lastDigit
        print(f'Sum={sum}')

def Part2():
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        sum = 0
        for line in lines:
            firstVal = 0
            firstPos = math.inf
            lastVal = 0
            lastPos = -math.inf
            for d in digits:
                if d in line:
                    for i in range(0, len(line)):
                        if (line[i] == d) and (i < firstPos):
                            firstVal = int(line[i]) * 10
                            firstPos = i
                    for i in range(len(line)-1, -1, -1):
                        if (line[i] == d) and (i > lastPos):
                            lastVal = int(line[i])
                            lastPos = i
            for e, n in enumerate(nums):
                if n in line:
                    for i in range(0, len(line) - (len(n) - 1)):
                        if (line[i:i+len(n)] == n) and (i < firstPos):
                            firstVal = int(e+1) * 10
                            firstPos = i
                    for i in range(len(line)-len(n), -1, -1):
                        if (line[i:i+len(n)] == n) and (i > lastPos):
                            lastVal = int(e+1)
                            lastPos = i
            sum += (firstVal + lastVal)
            print(f'Sum={sum}')

Part2()