def Part1():
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        sum = 0
        loadout = {'red': 12, 'green': 13, 'blue': 14}
        print(loadout)
        for i, line in enumerate(lines):
            reveals = line.split(':')[-1].split(';')
            valid = True
            for r in reveals:
                cubes = r.split(',')
                for c in cubes:
                    num = int(c[1:].split(' ')[0])
                    colour = c[1:].split(' ')[1]
                    print(f'Num={num} Colour={colour}')
                    if loadout[colour] < num:
                        valid = False
            if valid:
                sum += (i + 1)
                print('---')
            print('=================')
        print(f'Sum={sum}')

def Part2():
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        sum = 0
        for i, line in enumerate(lines):
            loadout = {'red': 0, 'green': 0, 'blue': 0}
            reveals = line.split(':')[-1].split(';')
            print(reveals)
            for r in reveals:
                cubes = r.split(',')
                for c in cubes:
                    num = int(c[1:].split(' ')[0])
                    colour = c[1:].split(' ')[1]
                    if loadout[colour] < num:
                        loadout[colour] = num
            power = loadout['red'] * loadout['green'] * loadout['blue']
            print(f'Power={power}')
            sum += power
            print('=================')
        print(f'Sum={sum}')    

# Part1()
Part2()