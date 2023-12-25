# Quicksort
# O(n*log_n)
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]  # recursive case
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([10, 5, 2, 3, 8, 20, 111, 243]))
