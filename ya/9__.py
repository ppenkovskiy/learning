def calculate_sum(N, M, Q, columns, table, constraints):
    result = 0

    col_index = {col: idx for idx, col in enumerate(columns)}

    valid_operators = {'<', '>'}

    int_constraints = [(col, op, int(value)) for col, op, value in constraints if op in valid_operators]

    for row in table:
        valid_cols = set(col for col, _, _ in int_constraints).intersection(row)

        flag = (row[col_index[col]] < value if op == '<' else row[col_index[col]] > value for col, op, value in int_constraints if col in valid_cols)

        result += sum(row) if all(flag) else 0

    return result

with open('9_input.txt', 'r') as file:
    N, M, Q = map(int, file.readline().split())
    columns = file.readline().split()
    table = [list(map(int, file.readline().split())) for _ in range(N)]
    constraints = [file.readline().split() for _ in range(Q)]

result = calculate_sum(N, M, Q, columns, table, constraints)
print(result)