import re

max_red = 12
max_green = 13
max_blue = 14

file = open("./input.txt", "r")
game_sum = 0

for line in file:
    line = line.strip()

    regex = r"^Game (\d+): (.*)$"
    game_id, game = re.findall(regex, line)[0]
    game = [subset.split(", ") for subset in game.split("; ")]

    valid = True
    for count, color in map(lambda pair: pair.split(), sum(game, [])):
        red = green = blue = 0
        count = int(count)

        match color:
            case "red":
                red += count
            case "green":
                green += count
            case "blue":
                blue += count
            case other:
                raise ValueError(f"Invalid color: {color}")

        if red > max_red or green > max_green or blue > max_blue:
            valid = False
            break

    if valid:
        game_sum += int(game_id)

print(game_sum)
file.close()
