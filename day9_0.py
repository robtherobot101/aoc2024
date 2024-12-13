from utils import get_input
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
    line = get_input("day9")[0]
    s = 0
    files = []
    spaces = []
    j = 0
    for file, space in [
        (int(line[i]), 0 if (i == len(line) - 1) else int(line[i + 1]))
        for i in range(0, len(line), 2)
    ]:
        files.append((j, file))
        j += file
        if space > 0:
            spaces.append((j, space))
            j += space

    for i in range(len(files), 0, -1):
        file_start, file_length = files[i - 1]
        if file_length == 0:
            continue
        for j, (space_start, space_length) in enumerate(spaces):
            if space_start >= file_start:
                break
            if file_length <= space_length:
                file_start = space_start
                space_length = space_length - file_length
                if space_length <= 0:
                    spaces.pop(j)
                else:
                    spaces[j] = (space_start + file_length, space_length)
                break
        for k in range(file_length):
            s += (i - 1) * (k + file_start)
    print(s)


if __name__ == "__main__":
    main()
