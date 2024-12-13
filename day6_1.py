from utils import get_input
from itertools import cycle
from time import perf_counter as perf_counter
from typing import Any


DIRS = cycle([(-1, 0), (0, 1), (1, 0), (0, -1)])

Q = cycle("^>v<")

a = set()


def profiler(method):
    def wrapper_method(*args: Any, **kwargs: Any) -> Any:
        t = perf_counter()
        ret = method(*args, **kwargs)
        print(f"Method {method.__name__} took : {perf_counter() - t:.3f} sec")
        return ret

    return wrapper_method


@profiler
def main():
    linesa = [[c if c != "." else "" for c in line] for line in get_input("input6_0")]
    for i in range(len(linesa)):
        if "^" in linesa[i]:
            pos = [i, linesa[i].index("^")]
            break
    check(linesa, DIRS, Q, pos)
    print(len(a))


def check(lines, dirs, q, pos, foo=False):
    d = next(dirs)
    sym = next(q)
    s = 0
    while True:
        lines[pos[0]][pos[1]] += sym
        if not 0 <= pos[0] + d[0] < len(lines) or not 0 <= pos[1] + d[1] < len(
            lines[0]
        ):
            return s
        n = lines[pos[0] + d[0]][pos[1] + d[1]]
        if sym in n:
            return foo
        if n in ("#", "O"):
            d = next(dirs)
            sym = next(q)
            continue
        if n == "" and not foo:
            lines2 = [line[:] for line in lines]
            lines2[pos[0] + d[0]][pos[1] + d[1]] = "O"
            if check(
                lines2,
                cycle([d, *[next(dirs) for _ in range(3)]]),
                cycle([sym, *[next(q) for _ in range(3)]]),
                pos[:],
                True,
            ):
                a.add((pos[0] + d[0], pos[1] + d[1]))
            next(dirs)
            next(q)
        pos[0] += d[0]
        pos[1] += d[1]


if __name__ == "__main__":
    main()
