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
    lines = get_input("input14")
    Y = 103
    X = 101

    points = []
    for line in lines:
        points.append([int(x) for x in re.findall(r'(-?\d+)', line)])

    i = 0
    while True:
        p = {}
        for point in points:
            point[0] = (point[0] + point[2]) % X
            point[1] = (point[1] + point[3]) % Y
            p[(point[0], point[1])] = "*"
        i += 1
        if (i - 29) % 101 == 0:
            print("\n".join("".join(("*" if (i, j) in p else ".") for i in range (X)) for j in range(Y)))
            print(i)
            input()




if __name__ == "__main__":
    main()
