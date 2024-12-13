import mpmath

from utils import get_input
from time import perf_counter as perf_counter
from typing import Any
import re


def profiler(method):
    def wrapper_method(*args: Any, **kwargs: Any) -> Any:
        t = perf_counter()
        ret = method(*args, **kwargs)
        print(f"Method {method.__name__} took : {perf_counter() - t:.3f} sec")
        return ret

    return wrapper_method


@profiler
def main():
    s = 0
    lines = iter(get_input("input13"))
    while line := next(lines, False):
        a = mpmath.matrix(
            list(
                zip(
                    [int(x) for x in re.findall(r"\+(\d+)", line)],
                    [int(x) for x in re.findall(r"\+(\d+)", next(lines))],
                )
            )
        )
        p = mpmath.matrix(
            [int(x) + 10000000000000 for x in re.findall(r"=(\d+)", next(lines))]
        )

        x, y = mpmath.qr_solve(a, p)[0]

        if mpmath.almosteq(x, round(x)) and mpmath.almosteq(y, round(y)):
            s += 3 * x + y

        if next(lines, None) is None:
            break
    print(s)


if __name__ == "__main__":
    main()
