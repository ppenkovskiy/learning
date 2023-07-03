def read_ints(path):
    with open(path, 'r', encoding='utf-8') as f:
        line = f.readlines()
    return line


def count_three_sum(ints):
    print('started count_three_sum')

    n = len(ints)
    counter = 0

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if ints[i] + ints[j] + ints[k] == 0:
                    counter += 1
                    print(f"Triple found: {ints[i]}, {ints[j]}, {ints[k]}.")
    print(f"Ended count_three_sum. Triplets counter = {counter}")


if __name__ == '__main__':
    print('Started main')

    ints = read_ints("..\\data\\1Kints.txt")
    count_three_sum(ints)

    print('What are we waiting for?')
    print("Ended main")




