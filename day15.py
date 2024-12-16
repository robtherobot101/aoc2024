from utils import get_input
from time import perf_counter as perf_counter
from typing import Any


dirs = {
    "v": [1, 0],
    ">": [0, 1],
    "^": [-1, 0],
    "<": [0, -1],
}


def profiler(method):
    def wrapper_method(*args: Any, **kwargs: Any) -> Any:
        t = perf_counter()
        ret = method(*args, **kwargs)
        print(f"Method {method.__name__} took : {perf_counter() - t:.3f} sec")
        return ret

    return wrapper_method


@profiler
def main():
    lines = get_input("input15test")
    m = [[c for c in line] for line in lines if line.startswith("#")]
    for i, line in enumerate(m):
        if "@" in line:
            pos = (i, line.index("@"))
            break

    d = [dirs[c] for line in lines for c in line if c in dirs]

    for direction in d:
        pos = push(pos, direction, m)
        print(direction)
        print("\n".join("".join(line) for line in m))
        # input()

    print("\n".join("".join(line) for line in m))
    s = 0
    for i, line in enumerate(m):
        for j, c in enumerate(line):
            if c == "O":
                s += (100 * i) + j
    print(s)


def push(pos, direction, m):
    c = m[pos[0]][pos[1]]
    if c == "#":
        return False
    if c == ".":
        return True
    if c == "O":
        if push((pos[0] + direction[0], pos[1] + direction[1]), direction, m):
            m[pos[0] + direction[0]][pos[1] + direction[1]] = c
            return True
        return False
    if c == "@":
        if push((pos[0] + direction[0], pos[1] + direction[1]), direction, m):
            m[pos[0] + direction[0]][pos[1] + direction[1]] = c
            m[pos[0]][pos[1]] = "."
            return (pos[0] + direction[0], pos[1] + direction[1])
        return pos
    raise ValueError(f"What da hell: {m[pos[0]][pos[1]]}")


if __name__ == "__main__":
    main()
