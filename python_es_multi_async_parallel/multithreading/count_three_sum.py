def read_ints(path):
    with open(path, 'r', encoding='utf-8') as f:
        line = [int(i.rstrip('\n').lstrip(' ')) for i in f.readlines()]
    return line


def count_three_sum(ints, thread_name='t'):
    print(f"Started count_three_sum in thread: {thread_name}.")
    n = len(ints)
    counter = 0

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if ints[i] + ints[j] + ints[k] == 0:
                    counter += 1
                    print(f"Triple found in {thread_name}: {ints[i]}, {ints[j]}, {ints[k]}.")

    print(f"Ended 'count_three_sum' in {thread_name}. Triplets counter = {counter}")
    return counter
