from utils import (get_input)

dirs = [
    [1, 0],
    [0, 1],
    [-1, 0],
    [0, -1],
    [1, 1],
    [1, -1],
    [-1, 1],
    [-1, -1]
]

def main():
    lines = get_input('input4_0test')
    print(lines)
    q = [[0 for _ in range(len(line))] for line in lines]
    s = 0
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            # t = 0
            # for direction in dirs:
            #     if check(lines, i, j, direction, "XMAS"):
            #         t += 1
            # q[j][i] = t
            # s += t
            s += check2(lines, i, j)
    print(s)
    print('\n'.join(str(x) for x in q))

def check(lines, x, y, direction, s):
    if s == "":
        return True
    if x < 0 or y < 0 or x >= len(lines) or y >= len(lines[x]) or lines[x][y] != s[0]:
        return False
    return check(lines, x+direction[0], y+direction[1], direction, s[1:])

def check2(lines, x, y):
    if x < 1 or y < 1 or x >= len(lines) - 1 or y >= len(lines[x]) - 1 or lines[x][y] != "A":
        return 0
    if lines[x-1][y+1] + lines[x+1][y-1] in ("MS", "SM") and lines[x + 1][y + 1] + lines[x - 1][y - 1] in ("MS", "SM"):
        return 1
    return 0




if __name__ == "__main__":
    main()
