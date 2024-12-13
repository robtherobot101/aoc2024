from utils import get_input


def main():
    lines = get_input("input1_0")[:-1]
    print(lines)
    print([line.split(" ")[0] for line in lines])
    a = sorted([int(line.split(" ")[0]) for line in lines])
    b = sorted([int(line.split(" ")[-1]) for line in lines])

    s = sum(abs(x - y) for x, y in zip(a, b))
    print(s)


if __name__ == "__main__":
    main()
