def Part1():
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        totalPoints = 0
        for i, line in enumerate(lines):
            winningNumbers = [int(x) for x in line.split(':')[1].split('|')[0].split(' ') if x != '']
            cardNumbers = [int(x) for x in line.split(':')[1].split('|')[1].split(' ') if x != '']
            matches = []
            points = 0
            for wn in winningNumbers:
                for cn in cardNumbers:
                    if cn == wn:
                        matches.append(cn)
            if len(matches) > 0:
                points = 2**(len(matches) - 1)
            totalPoints += points
        print(f'Total Points: {totalPoints}')

def Part2():
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        cards = {i+1: 1 for i in range(len(lines))}
        for i, line in enumerate(lines):
            print(f'About to scratch {cards[i+1]} * card {i+1}')
            # Calculate the number of matches, then multiply
            winningNumbers = [int(x) for x in line.split(':')[1].split('|')[0].split(' ') if x != '']
            cardNumbers = [int(x) for x in line.split(':')[1].split('|')[1].split(' ') if x != '']
            matches = 0
            for wn in winningNumbers:
                for cn in cardNumbers:
                    if cn == wn:
                        matches += 1
            for j in range(matches):
                cards[i+j+2] += cards[i+1]

            # for j in range(cards[i+1]):
            #     winningNumbers = [int(x) for x in line.split(':')[1].split('|')[0].split(' ') if x != '']
            #     cardNumbers = [int(x) for x in line.split(':')[1].split('|')[1].split(' ') if x != '']
            #     matches = 0
            #     for wn in winningNumbers:
            #         for cn in cardNumbers:
            #             if cn == wn:
            #                 matches += 1
            #     for k in range(matches):
            #         cards[i+k+2] += 1
        print(f'Total cards: {sum(cards.values())}')

# Part1()
Part2()