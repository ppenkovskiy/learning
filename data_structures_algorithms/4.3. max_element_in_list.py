def max_element_in_list(l):
    res = l[0]
    for i in range(len(l)):
        if l[i] > res:
            res = l[i]
    return res


print(max_element_in_list([1, 2, 3, 4, 5]))
    