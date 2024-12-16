from utils import get_input
from time import perf_counter as perf_counter
from typing import Any
from queue import PriorityQueue

from dataclasses import dataclass, field
from typing import Any


@dataclass(order=True)
class V:
    priority: int
    item: Any = field(compare=False)


dirs = (
    [1, 0],
    [0, 1],
    [-1, 0],
    [0, -1],
)


def profiler(method):
    def wrapper_method(*args: Any, **kwargs: Any) -> Any:
        t = perf_counter()
        ret = method(*args, **kwargs)
        print(f"Method {method.__name__} took : {perf_counter() - t:.3f} sec")
        return ret

    return wrapper_method


@profiler
def main():
    lines = get_input("input16")
    m = [[c for c in line] for line in lines if line.startswith("#")]
    for i, line in enumerate(m):
        if "E" in line:
            end = (i, line.index("E"))
    print(dijkstra(m, end))


def dijkstra(m, end):
    dist = {}
    prev = {}
    Q = PriorityQueue()
    for i, line in enumerate(m):
        for j, c in enumerate(line):
            for k in range(len(dirs)):
                if c == "S" and k == 1:
                    dist[(i, j, k)] = 0
                    Q.put((0, i, j, k))
                elif c in "SE.":
                    dist[(i, j, k)] = float("inf")
                    Q.put((float("inf"), i, j, k))
                if c == "E":
                    end = (i, j)

    while not Q.empty():
        u = tuple(Q.get()[1:])
        if (u[0], u[1]) == end:
            return dist[u]
        for i in range(-1, 2):
            d = (u[2] + i) % 4
            x = 1 - abs(i)
            v = (u[0] + dirs[d][0] * x, u[1] + dirs[d][1] * x, d)
            if m[v[0]][v[1]] == "#":
                continue
            alt = dist[u] + x + (1000 * abs(i))
            if alt < dist[v]:
                dist[v] = alt
                prev[(alt, *v)] = u
                Q.put((alt, *v))


if __name__ == "__main__":
    main()
