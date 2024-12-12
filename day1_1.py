from utils import (get_input)


def main():
    lines = get_input('input1_0')
    a = [int(line.split(" ")[0]) for line in lines]
    b = [int(line.split(" ")[-1]) for line in lines]

    print(a)
    print(b)
    s = sum(b.count(x) * x for x in a)
    print(s)


if __name__ == "__main__":
    main()
