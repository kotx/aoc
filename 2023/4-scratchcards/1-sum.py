total = 0
with open("./input.txt", "r") as file:
    for line in file:
        line = line.split(": ")[1]
        winning, actual = [x.split() for x in line.split(" | ")]
        won = sum([1 for x in winning if x in actual])
        if won > 0:
            total += pow(2, won-1)

print(total)