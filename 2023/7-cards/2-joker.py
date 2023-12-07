from collections import Counter
from functools import cmp_to_key

# fivekind: 6
# fourkind: 5
# fullhouse: 4
# threekind: 3
# twopair: 2
# onepair: 1
# highcard: 0

def score(hand: str) -> int:
    hand_counts = Counter(hand)
    type = 0
    possible_full_house = False

    for card, count in hand_counts.most_common():
        if count == 5:
            type = 6
            break
        if count == 4:
            type = 5
            break
        if count == 3:
            possible_full_house = True
            type = 3
        if count == 2:
            if possible_full_house:
                type = 4
                break
            if type == 1:
                type = 2
                break
            type = 1

    return type

def best_score(hand: str) -> int:
    if "J" in hand:
        return max(best_score(hand.replace("J", c, 1)) for c in ordering[:-1])
    return score(hand)

with open("./input.txt", "r") as file:
    ranks = []
    for line in file:
        hand, bid = line.split() 

        ranks.append((score(hand), hand, int(bid)))

    ordering = "AKQT98765432J"
    ranks = sorted(ranks, key=lambda x: (best_score(x[1]), [-ordering.index(c) for c in x[1]]))

    print(sum(rank[2]*(i+1) for i, rank in enumerate(ranks)))
