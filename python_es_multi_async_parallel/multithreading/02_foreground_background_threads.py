import threading

from count_three_sum import read_ints, count_three_sum

if __name__ == '__main__':
    print('Started main')

    ints = read_ints("..\\data\\1Kints.txt")
    t1 = threading.Thread(target=count_three_sum, args=(ints,), daemon=True)
    t1.start()

    print(input("What is your name?\n"))

    t1.join()

    print("Ended main")
