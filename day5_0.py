from utils import get_input
import itertools


def main():
    lines = iter(get_input("input5_0"))
    rules = list(itertools.takewhile(lambda x: x != "", lines))
    updates = list(lines)

    r = {}
    for rule in rules:
        x, y = [int(z) for z in rule.split("|")]
        r.setdefault(x, set()).add(y)

    s = 0
    for update in updates:
        update = [int(x) for x in update.split(",")]
        seen = []
        for n in update:
            if any(x in r.get(n, []) for x in seen):
                break
            seen.append(n)
        else:
            s += update[(len(update) // 2)]

    print(s)


if __name__ == "__main__":
    main()
