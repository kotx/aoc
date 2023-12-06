from math import prod

with open("./input.txt", "r") as file:
    times = map(int, file.readline().split()[1:])
    records = map(int, file.readline().split()[1:])
    races = zip(times, records)
    
    ways = []
    for time, record in races:
        ways_race = 0
        for i in range(time + 1):
            move_time = time - i
            dist = move_time * i
            if dist > record:
                ways_race += 1
        ways.append(ways_race)

    print(prod(ways))