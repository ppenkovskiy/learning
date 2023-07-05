import concurrent.futures
from count_three_sum import read_ints, count_three_sum

if __name__ == "__main__":
    print('Started main')

    data = read_ints("..\\data\\1Kints.txt")

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        results = executor.map(count_three_sum, (data, data), ('t1', 't2'))
        for r in results:
            print(f"{r=}")

    print('Ended main')
