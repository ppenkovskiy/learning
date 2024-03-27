# Square the numbers that are greater than zero.
# Multiply by 3 every third number.
# Multiply by -1 every fifth number.
# Return the sum of the sequence.

# Example
# { -2, -1, 0, 1, 2 } returns -6
# 1. { -2, -1, 0, 1 * 1, 2 * 2 }
# 2. { -2, -1, 0 * 3, 1, 4 }
# 3. { -2, -1, 0, 1, -1 * 4 }
# 4. -6

def calc(a):
    for i, n in enumerate(a):
        if a[i] > 0:
            a[i] *= a[i]
        if i % 3 == 2:
            a[i] = a[i] * 3
        if i % 5 == 4:
            a[i] = a[i] * -1
    return sum(a)


a = [-2, -1, 0, 1, 2]
print(calc(a))
