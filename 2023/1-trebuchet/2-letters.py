letter_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

with open("./input.txt", "r") as file:
    sum = 0
    for line in file:
        for word, digit in letter_map.items():
            line = line.replace(word, word+digit+word) # this trick allows for word overlap (e.g. fiveight = 58)

        digits = [c for c in line if c.isdigit()] # fixme: unnecessary processing of middle-values
        calibration = int(digits[0]+digits[-1])
        sum += calibration

    print(sum)
