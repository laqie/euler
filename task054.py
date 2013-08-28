from collections import Counter

CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
HAND_RANK = ['HC', 'OP', 'TP', 'TK', 'ST', 'FL', 'FH', 'FK', 'SF', 'RF']

RANKS = dict((card, index) for index, card in enumerate(CARDS + HAND_RANK))

def parse_hand(hand):
    cards = sorted([card[0] for card in hand], cmp=lambda x, y: RANKS[x] - RANKS[y])
    suits = sorted([card[1] for card in hand])
    return cards, suits


def is_flush(_, suits):
    return True if suits[0] == suits[-1] else False


def is_straight(cards, _):
    high_card = CARDS.index(cards[-1])
    if CARDS[high_card] == CARDS[-1]:
        if cards[:-1] == CARDS[:4]:
            return True
    if cards == CARDS[high_card - 4:high_card + 1]:
        return True
    return False

def is_royal(cards, suits):
    if is_flush(cards, suits) and is_straight(cards, suits) and cards[-1] == 'A' and cards[0] == 'T':
        return True
    return False

def is_straightflush(cards, suits):
    if is_flush(cards, suits) and is_straight(cards, suits):
        return True
    return False


def get_score(hand):
    cards, suits = parse_hand(hand)
    counter = Counter(cards)
    length = len(counter)
    high_card = cards[-1]

    if is_royal(cards, suits):
        return RANKS['RF']

    if is_straightflush(cards, suits):
        return RANKS['SF'] + RANKS[high_card] * 0.01

    if length == 2 and counter.most_common(1)[0][1] == 4:
        if counter.most_common(1)[0][0] == high_card:
            high_card1 = counter.most_common(2)[1][0]
        else:
            high_card1 = high_card
            high_card = counter.most_common(1)[0][0]
        return RANKS['FK'] + RANKS[high_card] * 0.01 + RANKS[high_card1] * 0.001

    if length == 2 and counter.most_common(1)[0][1] == 3:
        if counter.most_common(1)[0][0] == high_card:
            high_card1 = counter.most_common(2)[1][0]
        else:
            high_card1 = high_card
            high_card = counter.most_common(1)[0][0]

        return RANKS['FH'] + RANKS[high_card] * 0.01 + RANKS[high_card1] * 0.001

    if is_flush(cards, suits):

        return RANKS['FL'] + RANKS[high_card] * 0.01

    if is_straight(cards, suits):

        if high_card == 'A':
            high_card = '5'

        return RANKS['ST'] + RANKS[high_card] * 0.01

    if length == 3 and counter.most_common(1)[0][1] == 3:
        hand_card = counter.most_common(1)[0][0]

        if hand_card == high_card:
            high_card = sorted(
                [counter.most_common(3)[1][0], counter.most_common(3)[2][0]],
                cmp=lambda x, y: RANKS[x] - RANKS[y])[-1]

        return RANKS['TK'] + RANKS[hand_card] * 0.01 + RANKS[high_card] * 0.001

    if length == 3 and counter.most_common(1)[0][1] == 2:
        hand_card1 = counter.most_common(1)[0][0]
        hand_card2 = counter.most_common(2)[1][0]

        if high_card == hand_card1 or high_card == hand_card2:
            high_card = counter.most_common(3)[2][0]

        return RANKS['TP'] + (RANKS[hand_card1] + RANKS[hand_card2]) * 0.01 + RANKS[high_card] * 0.001


    if length == 4:
        hand_card = counter.most_common(1)[0][0]
        if hand_card == high_card:
            high_card = sorted(
                [counter.most_common(4)[1][0], counter.most_common(4)[2][0], counter.most_common(4)[2][0]],
                cmp=lambda x, y: RANKS[x] - RANKS[y])[-1]
        return RANKS['OP'] + RANKS[hand_card] * 0.01 + RANKS[high_card] * 0.001

    return RANKS[high_card] * 0.01


with open('poker.txt') as f:
    hands = map(str.split, f.readlines())

print len(filter(lambda game: get_score(game[:5]) > get_score(game[5:]), hands))
