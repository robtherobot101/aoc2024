from utils import (get_input)
from itertools import cycle

dirs = cycle(
    [(-1, 0),
    (0, 1),
    (1, 0),
    (0, -1)]
)

q = cycle('^>v<')

def main():
    lines = [[[c] if  c != '.' else list() for c in line ] for line in get_input('input6_0')]
    for i in range(len(lines)):
        if ['^'] in lines[i]:
            pos = [i, lines[i].index(['^'])]
            lines[pos[0]][pos[1]] = []
            break
    d = next(dirs)
    sym = next(q)
    while True:
        # print('\n'.join(str(x) for x in lines))
        # print()
        lines[pos[0]][pos[1]].append(sym)
        if not 0 <= pos[0] + d[0] < len(lines) or not 0 <= pos[1] + d[1] < len(lines[0]):
            break
        n = lines[pos[0] + d[0]][pos[1] + d[1]]
        if sym in n:
            break
        elif '#' in n:
            d = next(dirs)
            sym = next(q)
            continue
        pos[0] += d[0]
        pos[1] += d[1]
    print('\n'.join(str(x) for x in lines))
    print(sum(1 for line in lines for x in line if any(y in x for y in '^>v<')))




if __name__ == "__main__":
    main()
