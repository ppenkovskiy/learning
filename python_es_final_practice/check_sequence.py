def check_sequence(l):
    if sorted(l) == l and len(set(l)) == len(l):
        return 1
    elif sorted(l, reverse=True) == l and len(set(l)) == len(l):
        return -1
    else:
        return 0