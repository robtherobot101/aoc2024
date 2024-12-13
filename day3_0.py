import re


def main():
    with open("inputs/input3_0") as f:
        s = f.read()

    # s = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

    s = s.split("do()")
    ss = ""
    for x in s:
        print(s)
        if "don't()" in x:
            print(x)
            ss += x[: x.index("don't()")]
        else:
            ss += x

    m = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", ss)

    print(sum(int(x) * int(y) for x, y in m))


if __name__ == "__main__":
    main()
