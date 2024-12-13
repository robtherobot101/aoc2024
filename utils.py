def get_input(filename):
    with open(f"inputs/{filename}") as fp:
        s = [x[:-1] for x in fp.readlines()]
    return s
