def Col(pattern, idx): 
    col = []
    for row in pattern:
        col.append(row[idx])
    return col

def Differences(v1, v2):
    assert len(v1) == len(v2)
    diffs = 0
    for i in range(len(v1)):
        if v1[i] != v2[i]:
            diffs += 1
    return diffs

def Day13():

    # EXPECTED_DIFFERENCES = 0 # Part1
    EXPECTED_DIFFERENCES = 1 # Part2

    lines = [] 
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    patterns = [[]]
    for line in lines:
        if line == '':
            patterns.append([])
        else:
            patterns[-1].append(line)

    result = 0

    for pattern in patterns:
        for row in pattern:
            print(row)
        # Check for horizontal symmetry
        hs = False
        for i in range(len(pattern)-1):
            differences = 0
            print(f'Checking for horizontal symmetry at rows {i}:{i+1}')
            for j in range(min(i+1, len(pattern)-i-1)):
                print(f'Checking rows {i-j} and {i+1+j}')
                # if pattern[i-j] != pattern[i+1+j]:
                d = Differences(pattern[i-j], pattern[i+1+j])
                print(f'\tDifferences: {d}')
                differences += d
            if differences == EXPECTED_DIFFERENCES:
                print(f'***** Detected horizontal symmetry at rows {i}:{i+1}*****')
                result += (i+1) * 100
                hs = True
                break
        if hs == False:
            print('No horizontal symmetry detected')
        print()
        # Check for vertical symmetry
        if hs == False:
            vs = False
            colLength = len(pattern[0])
            for i in range(colLength-1):
                differences = 0
                print(f'Checking for vertical symmetry at cols {i}:{i+1}')
                for j in range(min(i+1, colLength-i-1)):
                    print(f'Checking cols {i-j} and {i+1+j}')
                    d = Differences(Col(pattern, i-j), Col(pattern, i+1+j))
                    print(f'\tDifferences: {d}')
                    differences += d
                if differences == EXPECTED_DIFFERENCES:
                    print(f'***** Detected vertical symmetry at cols {i}:{i+1} *****')
                    result += (i+1)
                    vs = True
                    break
            if vs == False:
                print('No vertical symmetry detected')

    print(f'Result={result}')

Day13()