# Binary search
# O(log_n)
# Бинарный поиск выполняется за логирифмическое время.
def binary_search(list, item):
    low_indx = 0
    high_indx = len(list) - 1

    while low_indx <= high_indx:
        mid_indx = int((low_indx + high_indx) / 2)
        guess = list[mid_indx]
        if guess == item:
            return mid_indx
        if guess > item:
            high_indx = mid_indx - 1
        else:
            low_indx = mid_indx + 1
    return None


my_list = [1, 3, 5, 7, 9, 10, 11, 20, 50, 60, 70]
print(binary_search(my_list, 70))
print(binary_search(my_list, -1))


# Number of iterations in binary search
import math
print(int(math.log2(128)))
print(int(math.log2(256)))
print(math.log2(100))
print(math.log2(10000))
print(math.log2(1000000000))
