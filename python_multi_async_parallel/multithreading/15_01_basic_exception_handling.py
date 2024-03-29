import threading
import time

throw = False


def count():
    i = 0
    try:
        while True:
            if throw:
                raise ZeroDivisionError()
            i += 1

            print(f"{i=}")
            time.sleep(1)
    except ZeroDivisionError:
        print('Exception occured')


if __name__ == '__main__':
    print('Started main')
    t1 = threading.Thread(target=count)
    t1.start()
    time.sleep(2)
    throw = True
    for x in range(1,5):
        print(f"{x=}")
        time.sleep(1)
    print('Ended main')