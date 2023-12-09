handNames = ['High Card', 'One Pair', 'Two Pairs', 'Three of a Kind', 'Full House', 
          'Four of a Kind', 'Five of a Kind']

cardMap = {
    'T': 'A',
    'J': 'B',
    'Q': 'C',
    'K': 'D',
    'A': 'E'
}

cardMap_2 = {
    'T': 'A',
    'Q': 'B',
    'K': 'C',
    'A': 'D',
    'J': '1'
}

def HandType(cards):
    countsByCard = {}
    for card in cards:
        if card in countsByCard.keys():
            countsByCard[card] += 1
        else:
            countsByCard[card] = 1
    counts = list(countsByCard.values())
    counts.sort(reverse=True)
    # print(f'Cards: {cards} counts: {counts}')
    if counts == [1, 1, 1, 1, 1]:
        return 0
    elif counts == [2, 1, 1, 1]:
        return 1
    elif counts == [2, 2, 1]:
        return 2
    elif counts == [3, 1, 1]:
        return 3
    elif counts == [3, 2]:
        return 4
    elif counts == [4, 1]:
        return 5
    elif counts == [5]:
        return 6
    else:
        print(f'cards: {cards}')
        print(f'counts: {counts}')
        assert False

def HandType_2(cards):
    countsByCard = {}
    for card in cards:
        if card != 'J':
            if card in countsByCard.keys():
                countsByCard[card] += 1
            else:
                countsByCard[card] = 1
    counts = list(countsByCard.values())
    counts.sort(reverse=True)

    # Add jokers
    if len(counts) == 0:
        counts = [5]
    else:
        for card in cards:
            if card == 'J':
                counts[0] += 1

    # print(f'Cards: {cards} counts: {counts}')
    if counts == [1, 1, 1, 1, 1]:
        return 0
    elif counts == [2, 1, 1, 1]:
        return 1
    elif counts == [2, 2, 1]:
        return 2
    elif counts == [3, 1, 1]:
        return 3
    elif counts == [3, 2]:
        return 4
    elif counts == [4, 1]:
        return 5
    elif counts == [5]:
        return 6
    else:
        print(f'cards: {cards}')
        print(f'counts: {counts}')
        assert False

def MapCards(cards):
    mappedCards = ''
    for c in cards:
        if c in cardMap.keys():
            mappedCards += cardMap[c]
        else:
            mappedCards += c
    return mappedCards

def MapCards_2(cards):
    mappedCards = ''
    for c in cards:
        if c in cardMap_2.keys():
            mappedCards += cardMap_2[c]
        else:
            mappedCards += c
    return mappedCards

def ScoreHand(cards):
    return str(HandType(cards)) + MapCards(cards)

def ScoreHand_2(cards):
    handType = HandType_2(cards)
    print(f'{cards} is {handNames[handType]}')
    return str(HandType_2(cards)) + MapCards_2(cards)

def Part1():
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        hands = []
        for line in lines:
            tokens = line.split(' ')
            hands.append([tokens[0], int(tokens[1])])
        # for hand in hands:
        #     print(f'{hand[0]}: {handNames[HandType(hand[0])]}')
        #     print(f'{hand[0]} -> {ScoreHand(hand[0])}')
        # print(hands, end='\n')
        hands.sort(key=lambda x: ScoreHand(x[0]))
        # print(hands)
        # Determine winnings
        winnings = 0
        for i in range(len(hands)):
            winnings += hands[i][1] * (i+1)
        print(f'Winnings: {winnings}')

def Part2():
    with open('input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        hands = []
        for line in lines:
            tokens = line.split(' ')
            hands.append([tokens[0], int(tokens[1])])
        hands.sort(key=lambda x: ScoreHand_2(x[0]))
        winnings = 0
        for i in range(len(hands)):
            winnings += hands[i][1] * (i+1)
        print(f'Winnings: {winnings}')

# Part1()
Part2()