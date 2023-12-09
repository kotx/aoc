import itertools

with open("./input.txt", "r") as file:
    s = 0
    for line in file:
        values = list(map(int, line.split())) 
        diffs = [values]
        while not all(v == 0 for v in diffs[-1]):
            diff = []
            for a, b in itertools.pairwise(diffs[-1]):
                diff.append(b - a)
            diffs.append(diff)
        del diff

        diffs[-1].append(0)
        # print(diffs)

        for idx in range(len(diffs)-2, -1, -1):
            # print("i", idx)
            x = diffs[idx][0] - diffs[idx+1][0]
            # print("x", x)
            diffs[idx].insert(0, x)

        # print(diffs)
        s += x

    print(s)
