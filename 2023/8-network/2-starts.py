# this solution is too slow.
# ended up checking reddit for solution

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
    steps = 0

    locs = [node for node in network if node.endswith("A")]
    found_zs = False
    while not found_zs:
        for i in instructions:
            steps += 1
            locs = [next_location[(loc, i)] for loc in locs]
        found_zs = all(loc.endswith("Z") for loc in locs)

    print(steps)
