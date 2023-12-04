from typing import Tuple


def is_sym(c: str):
    assert len(c) == 1
    return c in "+@-&#%$*=/"

with open("./input.txt", "r") as file:
    sum = 0
    lines = file.readlines()
    for y, line in enumerate(lines):
        line = line.strip()
        found_sym = False
        num_span: Tuple[int, int] | None = None # (start, end)
        for x, char in enumerate(line+"."):
            if char.isdigit():
                digit = int(char)
                if num_span is None:
                    num_span = (x, x)
                else:
                    num_span = (num_span[0], x)
            else:
                if found_sym and num_span is not None:
                    found_num = line[num_span[0]:num_span[1]+1]
                    # print(y, found_num)
                    sum += int(found_num)
                num_span = None
                found_sym = False

            if num_span is None or found_sym: continue

            # Look for adjacent symbols
            up = y != 0 and is_sym(lines[y-1][x])
            down = y != len(lines) - 1 and is_sym(lines[y+1][x])

            def check_triple(x):
                x_mid = is_sym(line[x])
                x_up = y != 0 and is_sym(lines[y-1][x])
                x_down = y != len(lines) - 1 and is_sym(lines[y+1][x])
                return x_mid or x_up or x_down

            # Check left/right if on edges
            left = x != 0 and num_span[1] == x and check_triple(x-1)
            right = x != len(line) - 1 and check_triple(x+1)

            # print(up, down, left, right)
            found_sym = up or down or left or right

    print(sum)