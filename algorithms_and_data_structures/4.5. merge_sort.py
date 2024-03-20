# merge sort
# сортировка слиянием
# О(п log п)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # divide the array into two equal parts
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # recursively sort each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # combining the sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    # comparing the elements of the left and right half
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    # add the remaining elements from the left half (if exist)
    while left_idx < len(left):
        result.append(left[left_idx])
        left_idx += 1

    # add the remaining elements from the right half (if exist)
    while right_idx < len(right):
        result.append(right[right_idx])
        right_idx += 1

    return result


# usage example
arr = [5, 3, 8, 6, 2, 7, 1, 4]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
