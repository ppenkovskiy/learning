def find_similarity(arr1, arr2):
    similarity = 0
    min_len = min(len(arr1), len(arr2))
    for i in range(min_len):
        if arr1[i] == arr2[i]:
            similarity += 1
        else:
            break
    return similarity

with open('input.txt', 'r') as file:
    n = int(file.readline())

    matrix = []
    for _ in range(n):
        n_elements = file.readline().rstrip('\n')
        elements = file.readline().split()
        matrix.append(elements)

    res = 0
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            res += find_similarity(matrix[i], matrix[j])

    print(res)