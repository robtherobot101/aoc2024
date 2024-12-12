from utils import (get_input)
from time import perf_counter as perf_counter
from typing import Any
import itertools
import operator

def profiler(method):
    def wrapper_method(*args: Any, **kwargs: Any) -> Any:
        t = perf_counter()
        ret = method(*args, **kwargs)
        print(f"Method {method.__name__} took : {perf_counter() - t:.3f} sec")
        return ret

    return wrapper_method


@profiler
def main():
    lines = [[c for c in line] for line in get_input('input8')]
    antennae = {}
    antinodes = set()

    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c.isalnum():
                antennae.setdefault(c, []).append((i, j))

    for freq, coords in antennae.items():
        for a, b in itertools.combinations(coords, 2):
            a1 = (a[0] - (b[0] - a[0]), a[1] - (b[1] - a[1]))
            a2 = (a[0] + 2 * (b[0] - a[0]), a[1] + 2 * (b[1] - a[1]))
            if 0 <= a1[0] < len(lines) and 0 <= a1[1] < len(lines[0]):
                lines[a1[0]][a1[1]] = '#'
                antinodes.add(a1)
            if 0 <= a2[0] < len(lines) and 0 <= a2[1] < len(lines[0]):
                lines[a2[0]][a2[1]] = '#'
                antinodes.add(a2)
    print(len(antinodes))
    print('\n'.join(''.join(y for y in x) for x in lines))

if __name__ == "__main__":
    main()
