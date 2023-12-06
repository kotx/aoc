with open("./input.txt", "r") as file:
    seeds = list(map(int, file.readline()[len("seeds: ") - 1 :].split()))
    locations = []

    line = file.readline()
    while line != "":
        # print("S", seeds)
        file.readline()
        line = file.readline()
        ranges = []  # [(start, end, delta)]
        while line != "\n" and line != "":
            # print("L", line, end="")
            dest_y, src_x, len = map(int, line.split())
            ranges.append((src_x, src_x + len - 1, dest_y - src_x))
            line = file.readline()

        for i, seed in enumerate(seeds):
            # print("s", seed)
            for offset in ranges:
                # print("O", offset)
                if offset[0] <= seed <= offset[1]:
                    seeds[i] = seed + offset[2]
                    break

    # print("S", seeds)
    print(min(seeds))
