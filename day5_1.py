from utils import get_input
import itertools
import functools


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
                l = sorted(
                    update,
                    key=functools.cmp_to_key(
                        lambda a, b: 1 if a in r.get(b, []) else -1
                    ),
                )
                s += l[(len(l) // 2)]
                break
            seen.append(n)

    print(s)


if __name__ == "__main__":
    main()
