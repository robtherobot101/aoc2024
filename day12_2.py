from utils import get_input
from time import perf_counter as perf_counter
from typing import Any
from itertools import pairwise, cycle

dirs = [
    [1, 0],
    [0, 1],
    [-1, 0],
    [0, -1],
]


def profiler(method):
    def wrapper_method(*args: Any, **kwargs: Any) -> Any:
        t = perf_counter()
        ret = method(*args, **kwargs)
        print(f"Method {method.__name__} took : {perf_counter() - t:.3f} sec")
        return ret

    return wrapper_method


@profiler
def main():
    lines = [[c for c in line] for line in get_input("day12")]
    visited = [[False for _ in line] for line in lines]
    s = 0
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if not visited[i][j]:
                x = flood_fill(lines, visited, c, (i, j))
                print(f"{c}: {x[0]} * {x[1]}")
                s += x[0] * x[1]
    print(s)


def flood_fill(garden, visited, c, pos):
    a = 0
    s = 0
    t = [pos]
    visited[pos[0]][pos[1]] = True
    while t:
        pos = t.pop()
        a += 1
        for i, d in enumerate(dirs):
            n_pos = (pos[0] + d[0], pos[1] + d[1])
            if (
                0 <= n_pos[0] < len(garden)
                and 0 <= n_pos[1] < len(garden[n_pos[0]])
                and garden[n_pos[0]][n_pos[1]] == c
            ):
                if not visited[n_pos[0]][n_pos[1]]:
                    t.append(n_pos)
                    visited[n_pos[0]][n_pos[1]] = True
        for m, n in ((dirs[x], dirs[(x + 1) % 4]) for x in range(len(dirs))):
            if (
                (
                    0 <= pos[0] + m[0] < len(garden)
                    and 0 <= pos[1] + m[1] < len(garden[0])
                    and garden[pos[0] + m[0]][pos[1] + m[1]] == c
                )
                and (
                    0 <= pos[0] + n[0] < len(garden)
                    and 0 <= pos[1] + n[1] < len(garden[0])
                    and garden[pos[0] + n[0]][pos[1] + n[1]] == c
                )
                and (
                    not (0 <= pos[0] + (m[0] if m[0] != 0 else n[0]) < len(garden))
                    or not (
                        0 <= pos[1] + (m[1] if m[1] != 0 else n[1]) < len(garden[0])
                    )
                    or (
                        garden[pos[0] + (m[0] if m[0] != 0 else n[0])][
                            pos[1] + (m[1] if m[1] != 0 else n[1])
                        ]
                        != c
                    )
                )
            ) or (
                (
                    (
                        not (0 <= pos[0] + m[0] < len(garden))
                        or not (0 <= pos[1] + m[1] < len(garden[0]))
                    )
                    or garden[pos[0] + m[0]][pos[1] + m[1]] != c
                )
                and (
                    (
                        not (0 <= pos[0] + n[0] < len(garden))
                        or not (0 <= pos[1] + n[1] < len(garden[0]))
                    )
                    or garden[pos[0] + n[0]][pos[1] + n[1]] != c
                )
            ):
                print(True)
                s += 1
    return a, s


if __name__ == "__main__":
    main()
