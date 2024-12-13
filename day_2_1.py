from utils import get_input


def main():
    lines = [[int(x) for x in line.split(" ")] for line in get_input("input2_0")]
    s = 0
    for line in lines:
        diffs = [line[i] - line[i + 1] for i in range(len(line) - 1)]
        if all(0 < x < 4 for x in diffs) or all(0 < -x < 4 for x in diffs):
            s += 1
            continue
        for j in range(len(line)):
            l2 = [x for i, x in enumerate(line) if j != i]
            diffs = [l2[i] - l2[i + 1] for i in range(len(l2) - 1)]
            if all(0 < x < 4 for x in diffs) or all(0 < -x < 4 for x in diffs):
                s += 1
                break
    print(s)


if __name__ == "__main__":
    main()
