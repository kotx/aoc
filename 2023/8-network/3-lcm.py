# optimized solution after checking reddit
# reference: https://www.reddit.com/r/adventofcode/comments/18dfpub/2023_day_8_part_2_why_is_spoiler_correct/

import itertools
import math

with open("./input.txt", "r") as file:
    instructions = file.readline().rstrip()

    file.readline()
    network = {}
    first = True
    loc = None
    for line in file:
        splits = line.split()
        name, left, right =  splits[0], splits[2][1:-1], splits[3][:-1] 
        if first:
            loc = (left, right)
            first = False
        network[name] = (left, right)

    next_location = {(loc, instruction): network[loc]["LR".index(instruction)] for loc in network for instruction in "LR"}

    locs = [node for node in network if node.endswith("A")]
    steps_set = set()
    for loc in locs:
        node = loc
        steps = 0
        for i in itertools.cycle(instructions):
            if node.endswith("Z"):
                steps_set.add(steps)
                break

            steps += 1
            node = next_location[(node, i)]
            

    print(math.lcm(*steps_set))
