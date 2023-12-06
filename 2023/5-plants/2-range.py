# Python is really slow to bruteforce with so I tried a smarter algorithm
# until I realized seeds can be affected by multiple offsets, which is complicated
# I took a solution that was quite impressive and used recursion.
# reference: https://advent-of-code.xavd.id/writeups/2023/day/5/
import itertools


with open("./input.txt", "r") as file:
    seed_ranges = map(int, file.readline()[len("seeds: ")-1:].split())
    seed_ranges = list(map(lambda x: range(x[0], x[0]+x[1]), itertools.batched(seed_ranges, 2)))
    file.readline()

    def read_range_map() -> list[(range, int)]:
        file.readline() # skip header
        map_data = []
        while line := file.readline():
            try:
                dest_y, src_x, count = map(int, line.split())
            except ValueError:
                break
            map_data.append((range(src_x, src_x + count), dest_y - src_x))
        return sorted(map_data, key=lambda x: x[0].start)
    
    def overlaps(a: range, b: range) -> bool:
        return a.start < b.stop and b.start < a.stop
    
    def add_range(r: range, d: int) -> range:
        return range(r.start + d, r.stop + d)
    
    def get_intersection(base: range, offsets: list[tuple[range, int]]) -> list[range]:
        for dest, offset in offsets:
            if not overlaps(base, dest): continue

            # () signifies base, [] signifies offset
            if dest.start <= base.start and base.stop <= dest.stop: # [()] inside offset
                return [add_range(base, offset)]

            if base.start <= dest.start and dest.stop <= base.stop: # ([]) overlap in middle
                return [range(base.start, dest.start), add_range(dest, offset), *get_intersection(range(dest.stop, base.stop), offsets)]

            if dest.start <= base.start and dest.stop <= base.stop: # [(]) overlap on left
                return [add_range(range(base.start, dest.stop), offset), *get_intersection(range(dest.stop, base.stop), offsets)]

            if base.start <= dest.start and base.stop <= dest.stop: # ([)] overlap on right
                return [range(base.start, dest.start), add_range(range(dest.start, base.stop), offset)]

        return [base]
                
    map_chunks = []
    while _map_chunk := read_range_map():
        map_chunks.append(_map_chunk)
    
    results = []
    for seed_range in seed_ranges:
        y_ranges = [seed_range]

        for chunk in map_chunks:
            y_ranges = list(
                    itertools.chain.from_iterable(get_intersection(y_range, chunk) for y_range in y_ranges)
            )

        results.append(sorted(y_ranges, key=lambda r: r.start)[0].start)

    print(min(results))
