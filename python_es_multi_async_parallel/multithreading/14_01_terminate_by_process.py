import multiprocessing
import time

from count_three_sum import read_ints, count_three_sum

if __name__ == '__main__':
    print('Started main')
    ints = read_ints("..\\data\\1Kints.txt")

    p = multiprocessing.Process(target=count_three_sum, args=(ints,))
    p.start()

    time.sleep(3)

    p.terminate()

    print('Ended main')
