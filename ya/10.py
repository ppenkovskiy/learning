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
        matrix.append([n_elements, elements])

    pairs = []
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            pairs.append([matrix[i][1], matrix[j][1]])

    res = 0
    for pair in pairs:
        res += find_similarity(pair[0], pair[1])
    print(res)