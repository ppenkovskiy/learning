def calculate_sum(N, M, Q, columns, table, constraints):

    result = 0

    for i in range(len(table)):
        flag = []
        for j in range(len(table[i])):
            for constraint in constraints:
                column_name, operator, value = constraint[0], constraint[1], int(constraint[2])
                if j == columns.index(column_name):
                    if operator == '<':
                        flag.append(table[i][j] < value)
                    elif operator == '>':
                        flag.append(table[i][j] > value)
        result += sum(table[i]) if all(flag) else 0
    return result

with open('9_input.txt', 'r') as file:
    N, M, Q = map(int, file.readline().split())
    columns = file.readline().split()
    table = [list(map(int, file.readline().split())) for _ in range(N)]
    constraints = [file.readline().split() for _ in range(Q)]

result = calculate_sum(N, M, Q, columns, table, constraints)
print(result)
