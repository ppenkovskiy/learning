# Simple search
# O(n)
def simple_search(matrix, value):
    for i in range(len(matrix)):
        if matrix[i] == value:
            return f"Index of your value in list is {i}."
    return "Your value doesn't exist"


matrix = [1, 2, 3, 4, 5]
value = 4

print(simple_search(matrix, value))
