with open("./input.txt", "r") as file:
    sum = 0
    for line in file:
        digits = [c for c in line if c.isdigit()]
        calibration = int(digits[0]+digits[-1])
        sum += calibration

    print(sum)
