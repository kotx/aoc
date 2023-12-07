from collections import Counter
from functools import cmp_to_key

with open("./input.txt", "r") as file:
    games = []
    ranks = []
    for line in file:
        hand, bid = line.split() 

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
                    if type == 1: # onepair
                        type = 2
                        break
                    type = 1 # onepair

            return type

        ranks.append((score(hand), hand, int(bid)))

    ordering = "AKQT98765432J"
    def best_score(hand: str) -> int:
        if "J" in hand:
            return max(best_score(hand.replace("J", c, 1)) for c in ordering[:-1])
        return score(hand)

    def compare(x, y):
        if x[0] == y[0]:
            for i in range(5):
                d = ordering.index(x[1][i]) - ordering.index(y[1][i])
                if d != 0:
                    return -d

        return x[0] - y[0]

    ranks = [(best_score(rank[1]), rank[1], rank[2]) for rank in ranks]
    ranks = sorted(ranks, key=cmp_to_key(compare))

    s = 0
    for i, rank in enumerate(ranks):
        bid = rank[2]
        s += (i+1)*bid

    print(s)
