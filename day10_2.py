from utils import get_input
from time import perf_counter as perf_counter
from typing import Any
import itertools
import math


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
    topo = [
        [-1 if c == "." else int(c) for c in line] for line in get_input("day10test")
    ]
    starts = [
        (i, j) for i in range(len(topo)) for j in range(len(topo[i])) if topo[i][j] == 0
    ]
    print(sum(bfs(start, 0, topo) for start in starts))


def bfs(pos, height, graph):
    if height == 9:
        return 1
    s = 0
    for d in dirs:
        n_pos = (pos[0] + d[0], pos[1] + d[1])
        if (
            0 <= n_pos[0] < len(graph)
            and 0 <= n_pos[1] < len(graph[0])
            and graph[n_pos[0]][n_pos[1]] == height + 1
        ):
            s += bfs(n_pos, height + 1, graph)
    return s


if __name__ == "__main__":
    main()
