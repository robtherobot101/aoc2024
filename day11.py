from utils import get_input
from time import perf_counter as perf_counter
from typing import Any
from functools import cache


def profiler(method):
    def wrapper_method(*args: Any, **kwargs: Any) -> Any:
        t = perf_counter()
        ret = method(*args, **kwargs)
        print(f"Method {method.__name__} took : {perf_counter() - t:.3f} sec")
        return ret

    return wrapper_method


@profiler
def main():
    line = get_input("input11")[0].split(" ")
    print(sum(do(stone, 75) for stone in line))


@cache
def do(stone, i):
    if i == 0:
        return 1
    if stone == "0":
        return do("1", i - 1)
    if len(stone) % 2 == 0:
        return do(stone[: len(stone) // 2], i - 1) + do(
            str(int(stone[len(stone) // 2 :])), i - 1
        )
    return do(str(int(stone) * 2024), i - 1)


if __name__ == "__main__":
    main()
