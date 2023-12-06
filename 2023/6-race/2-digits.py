with open("./input.txt", "r") as file:
    time = int("".join(file.readline().split()[1:]))
    record = int("".join(file.readline().split()[1:]))
    
    ways = 0
    for i in range(time + 1):
        move_time = time - i
        dist = move_time * i
        if dist > record:
            ways += 1

    print(ways)