from typing import Dict, List, Tuple
from math import prod


with open("./input.txt", "r") as file:
    sym_to_nums: Dict[Tuple[int, int], List[int]] = {}
    lines = file.readlines()
    for y, line in enumerate(lines):
        line = line.strip()
        found_sym = False
        num_span: Tuple[int, int] | None = None # (start, end)
        found_symbols = []
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
                    for symbol in found_symbols:
                        sym_to_nums.setdefault(symbol, []).append(int(found_num))
                num_span = None
                found_sym = False
                found_symbols = []

            if num_span is None or found_sym: continue

            def is_sym(y, x):
                is_sym = lines[y][x] in "+@-&#%$*=/"
                if is_sym:
                    found_symbols.append((x, y))
                return is_sym

            # Look for adjacent symbols
            up = y != 0 and is_sym(y-1, x)
            down = y != len(lines) - 1 and is_sym(y+1, x)

            def check_triple(x):
                x_mid = is_sym(y, x)
                x_up = y != 0 and is_sym(y-1, x)
                x_down = y != len(lines) - 1 and is_sym(y+1, x)
                return x_mid or x_up or x_down

            # Check left/right if on edges
            left = x != 0 and num_span[1] == x and check_triple(x-1)
            right = x != len(line) - 1 and check_triple(x+1)

            # print(up, down, left, right)
            found_sym = up or down or left or right

    sum = 0
    print(sym_to_nums)
    for nums in sym_to_nums.values():
        if len(nums) == 2: sum += prod(nums)
    print(sum)