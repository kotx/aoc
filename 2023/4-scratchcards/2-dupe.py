from typing import Dict, List


line_wins = []

with open("./input.txt", "r") as file:
    for i, line in enumerate(file):
        line = line.split(": ")[1]
        winning, actual = [x.split() for x in line.split(" | ")]
        wins = sum([1 for x in winning if x in actual])
        line_wins.append(wins)

line_copies = [1 for x in line_wins]
for i, copies in enumerate(line_copies):
    wins = line_wins[i]
    line_copies[i+1:i+wins+1] = [x+copies for x in line_copies[i+1:i+wins+1]]

print(sum(line_copies))