def calculate_sum(N, M, Q, columns, table, constraints):
    result = 0

    col_index = {col: idx for idx, col in enumerate(columns)}

    valid_operators = {'<', '>'}

    for row in table:
        flag = [row[col_index[constraint[0]]] < int(constraint[2]) if constraint[1] == '<' else
                row[col_index[constraint[0]]] > int(constraint[2]) for constraint in constraints if
                constraint[1] in valid_operators]

        result += sum(row) if all(flag) else 0

    return result


with open('9_input.txt', 'r') as file:
    N, M, Q = map(int, file.readline().split())
    columns = file.readline().split()
    table = [list(map(int, file.readline().split())) for _ in range(N)]
    constraints = [file.readline().split() for _ in range(Q)]

result = calculate_sum(N, M, Q, columns, table, constraints)
print(result)
