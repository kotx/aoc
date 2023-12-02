import re

file = open("./input.txt", "r")
game_sum = 0

for line in file:
    line = line.strip()

    regex = r"^Game (\d+): (.*)$"
    game_id, game = re.findall(regex, line)[0]
    game = [subset.split(", ") for subset in game.split("; ")]

    game_red = game_green = game_blue = 0
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

        game_red = max(game_red, red)
        game_green = max(game_green, green)
        game_blue = max(game_blue, blue)

    game_sum += game_red * game_green * game_blue

print(game_sum)
file.close()
