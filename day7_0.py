from utils import get_input
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


ops = ["+", "*"]


@profiler
def main():
    lines = get_input("input7")
    ss = 0
    for i, line in enumerate(lines):
        t, s = line.split(":")
        t = int(t)
        n = [int(x) for x in s.split(" ") if x != ""]
        if check("+", n, t, 0) or check("*", n, t, 0):
            ss += t
        print(f"{i}: {ss}")
    print(ss)


def check(o, n, t, s=0):
    o = operator.add if o == "+" else operator.mul
    if t - s < 0:
        return False
    if len(n) == 0:
        return s == t
    return check("+", n[1:], t, o(s, n[0])) or check("*", n[1:], t, o(s, n[0]))


if __name__ == "__main__":
    main()
