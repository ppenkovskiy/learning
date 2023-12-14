def count(l):
    if l == []:
        return 0
    return 1 + count(l[1:])

print(count([1,2,3]))