import time

def ValidSequence(sequence, records):
    observed = []
    currentGroup = 0
    for c in sequence:
        if c == '#':
            currentGroup += 1
        elif c == '.' and currentGroup > 0:
            observed.append(currentGroup)
            currentGroup = 0
    if currentGroup > 0:
        observed.append(currentGroup)
    # print(f'Observed={observed} Recorded={records}')
    return observed == records

def MakeSequence(baseSeq, numUnknown, n):
    toInsert = format(n, f'0{numUnknown}b').replace('0', '.').replace('1', '#')
    insertCounter = 0
    testSeq = ''
    for c in baseSeq:
        if c != '?':
            testSeq += c
        else:
            testSeq += toInsert[insertCounter]
            insertCounter += 1
    return testSeq

def Part1():
    lines = []
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    springs = []
    for line in lines:
        toks = line.split(' ')
        baseSeq = toks[0]
        records = [int(x) for x in toks[1].split(',')]
        springs.append((baseSeq, records))

    result = 0
    for i, spring in enumerate(springs):
        # print(spring, end=' ')
        numUnknown = len([c for c in spring[0] if c == '?'])
        # print(f'Unknown: {numUnknown}')
        for j in range(0, 2**numUnknown):
            testSeq = MakeSequence(spring[0], numUnknown, j)
            if ValidSequence(testSeq, spring[1]):
                result += 1
            # print(f'j={j}, test={testSeq}')
        print(f'Done {i+1}')

    print(f'Result={result}')

def PlausibleSequence(idx, seq, obs, records, charsRequired):
    
    if len(obs) > len(records) : return False

    charsRemaining = len(seq) - idx - 1
    if charsRemaining < charsRequired: return False

    for i in range(len(obs)):
        if i < (len(obs)-1) and obs[i] != records[i]: return False
        elif i == (len(obs)-1) and obs[i] > records[i]: return False

    return True

def IterateSequence(idx, seq, obs, records, charsRequired):
    # print(f'\nIterateSequence(idx={idx}, seq={seq}, obs={obs} records={records})')

    # Terminating condition
    if idx == len(seq):
        if obs == records:
            # print(f'***** Found a valid sequence {seq} *****')
            return 1
        else:
            return 0

    # If the next character is known, update the observed arrangments and continue iterating
    # If the observed arrangements cannot fit the known record, abandon the search
    if seq[idx] == '#':
        if len(obs) == 0: 
            obs.append(1) # first arrangement
            charsRequired -= 1
        elif len(obs) > 0 and seq[idx-1] == '.': 
            obs.append(1) # new arrangement
            charsRequired -= 2
        elif len(obs) > 0 and seq[idx-1] == '#': 
            obs[-1] += 1  # continuing arrangement
            charsRequired -= 1
        # print(f'Obs of seq {seq} at idx {idx}: {obs}')
        if PlausibleSequence(idx, seq, obs, records, charsRequired):
            return IterateSequence(idx+1, seq, obs.copy(), records, charsRequired)
        else:
            # print('Not a plausible sequence, halting search')
            return 0
    elif seq[idx] == '.':
        return IterateSequence(idx+1, seq, obs.copy(), records, charsRequired)

    # If the next character is unknown, branch to two searches
    if seq[idx] == '?':
        seqA = seq[:idx] + '#' + seq[idx+1:]
        seqB = seq[:idx] + '.' + seq[idx+1:]
        # NB: Don't increment the index here...
        result = IterateSequence(idx, seqA, obs.copy(), records, charsRequired)
        result += IterateSequence(idx, seqB, obs.copy(), records, charsRequired)
        return result

def Part2():
    lines = []
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    springs = []
    for i, line in enumerate(lines):
        toks = line.split(' ')
        baseSeq = toks[0]
        records = [int(x) for x in toks[1].split(',')]
        unfoldedSeq = ''
        unfoldedRecords = []
        for j in range(5):
            unfoldedSeq += baseSeq
            if j < 4:
                unfoldedSeq += '?'
            unfoldedRecords += records
        # Calculate the minimum number of characters required to fulfil the record
        # This will help us stop searching early if it is impossible we can fill
        # the rest of the record with the characters remaining. Hopefully.
        baseCharsRequired = sum(records) + len(records) - 1
        unfoldedCharsRequired = sum(unfoldedRecords) + len(unfoldedRecords) - 1
        # springs.append((baseSeq, records, baseCharsRequired, i+1))
        springs.append((unfoldedSeq, unfoldedRecords, unfoldedCharsRequired, i+1))

    springs.sort(key=lambda x: len([c for c in x[0] if c == '?']), reverse=True)

    # Clearly a basic search is not going to work...
    start = time.time()
    result = IterateSequence(0, springs[0][0], [], springs[0][1], springs[0][2])
    end = time.time()
    print(f'Took {end-start} seconds... Result={result}')

    # for spring in springs:
    #     if '.' not in spring[0]:
    #         print(spring)

    # count = 0
    # for i, spring in enumerate(springs):
    #     numUnknown = len([x for x in spring[0] if x == '?'])
    #     print(f'Attempting a sequence with {numUnknown} unknown positions...')
    #     count += IterateSequence(0, spring[0], [], spring[1])
    #     print(f'Done {i+1}')
    # print(f'Result = {count}') 



Part2()