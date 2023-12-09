import math

def Part1():
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        times = [int(t) for t in lines[0].split(':')[1].split(' ') if t != '']
        distanceRecords = [int(d) for d in lines[1].split(':')[1].split(' ') if d != '']
        print(times)
        print(distanceRecords)
        betterTimes = []
        for i in range(len(times)):
            maxTime = times[i]
            distanceRecord = distanceRecords[i]
            betterCount = 0
            for holdTime in range(maxTime+1):
                distance = holdTime * (maxTime - holdTime)
                if distance > distanceRecord:
                    betterCount += 1
            betterTimes.append(betterCount)
        print(betterTimes)
        result = 1
        for ht in betterTimes:
            result *= ht
        print(result) 

def QuadraticFormula(a, b, c):
    x1 = (-b + math.sqrt(b**2 - (4*a*c))) / (2*a)
    x2 = (-b - math.sqrt(b**2 - (4*a*c))) / (2*a)
    return x1, x2

# x1, x2 = QuadraticFormula(1, -71530, 940200)

x1, x2 = QuadraticFormula(1, -49877895, 356137815021882)

print(x1)
print(x2)
lowest = int(min(x1, x2))
biggest = int(max(x1, x2))
print(biggest - lowest)


# Part1()