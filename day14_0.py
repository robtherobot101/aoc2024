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
    s = [[0, 0], [0, 0]]

    for line in lines:
        x, y, x_speed, y_speed = [int(x) for x in re.findall(r'(-?\d+)', line)]
        # print(f"{x}, {y}, {x_speed}, {y_speed}")
        x = (x + x_speed * 100) % X
        y = (y + y_speed * 100) % Y

        if not (((X % 2) and x == X // 2) or ((Y % 2) and y == Y // 2)):
            ax = 0 if x < X / 2 else 1
            ay = 0 if y < Y / 2 else 1
            print(f"{x}, {y}")
            s[ax][ay] += 1
    print(s)
    print(s[0][0] * s[0][1] * s[1][0] * s[1][1])




if __name__ == "__main__":
    main()
