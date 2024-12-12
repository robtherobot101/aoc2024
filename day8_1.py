from utils import (get_input)
from time import perf_counter as perf_counter
from typing import Any
import itertools
import math

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
    m = [['.' for _ in lines] for _ in lines[0]]
    antennae = {}
    antinodes = set()

    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c.isalnum():
                antennae.setdefault(c, []).append((i, j))

    for freq, coords in antennae.items():
        for a, b in itertools.combinations(coords, 2):
            delta = (a[0] - b[0], a[1] - b[1])
            delta = (delta[0] // math.gcd(*delta), delta[1] // math.gcd(*delta))

            i, j = a
            while 0 <= i < len(lines) and 0 <= j < len(lines[0]):
                m[i][j] = '#'
                i += delta[0]
                j += delta[1]
            i, j = a
            while 0 <= i < len(lines) and 0 <= j < len(lines[0]):
                m[i][j] = '#'
                i -= delta[0]
                j -= delta[1]


    m = '\n'.join(''.join(y for y in x) for x in m)
    print(m.count('#'))

if __name__ == "__main__":
    main()
