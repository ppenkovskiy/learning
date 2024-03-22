def generate(numRows):
    if numRows == 1:
        return [[1]]
    result = [[] * (i + 1) for i in range(numRows)]
    for i in range(len(result)):
        if i == 0:

            result[i] = [1]

        else:

            for j in range(i + 1):

                if j == 0:
                    result[i].append(1)
                elif j == i:
                    result[i].append(1)
                else:
                    result[i].append(result[i - 1][j - 1] + result[i - 1][j])

    return result


for i in range(1, 11):
    print(generate(i))
