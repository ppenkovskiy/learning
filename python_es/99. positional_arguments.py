def avg(a, b, c):
    return (a + b + c) / 3


print(avg(1, 2, 3))
print(avg(a=1, b=2, c=3))


def avg(a, b, c, /):
    return (a + b + c) / 3


print(avg(1, 2, 3))
# print(avg(a=1, b=2, c=3)) # raise an exception


def assert_equal(left, right, /, fail_messsage=''):  # before slash - positional only arguments
    return (left == right, fail_messsage)


print(assert_equal(1, 1))
print(assert_equal(1, 2, fail_messsage='left not'))


# finish later
    