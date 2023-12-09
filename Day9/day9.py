def NextElement(seq):
    seqs = [seq.copy()]
    while sum(seq) != 0:
        nextSeq = []
        for i in range(0, len(seq) - 1):
            nextSeq.append(seq[i+1] - seq[i])
        seqs.append(nextSeq)
        seq = nextSeq
    # for s in seqs:
    #     print(s)
    for i in range(1, len(seqs)):
        seqs[-i-1].append(seqs[-i-1][-1] + seqs[-i][-1])
    # for s in seqs:
    #     print(s)
    return seqs[0][-1]

def PreviousElement(seq):
    seqs = [seq.copy()]
    while sum(seq) != 0:
        nextSeq = []
        for i in range(0, len(seq) - 1):
            nextSeq.append(seq[i+1] - seq[i])
        seqs.append(nextSeq)
        seq = nextSeq
    for s in seqs:
        print(s)
    for i in range(1, len(seqs)):
        prevEl = seqs[-i-1][0] - seqs[-i][0]
        seqs[-i-1] = [prevEl] + seqs[-i-1]
    for s in seqs:
        print(s)
    print()
    return seqs[0][0]  

def Part1():
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        sequences = []
        answer = 0
        for line in lines:
            sequences.append([int(x) for x in line.split(' ')])
            answer += PreviousElement(sequences[-1])
        print(f'Answer={answer}')

Part1()