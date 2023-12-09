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

    loc = "AAA"
    found_zzz = False
    while not found_zzz:
        for i in instructions:
            next_loc = next_location[(loc, i)]
            steps += 1
            if next_loc == "ZZZ":
                found_zzz = True
                break
            loc = next_loc

    print(steps)
