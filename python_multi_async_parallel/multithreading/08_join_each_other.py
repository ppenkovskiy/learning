import threading
import time


def f1():
    print("Running 1st thread")
    print("f1 joining f2")
    time.sleep(1)
    t2.join()

    print('f1 sleep')
    time.sleep(2)
    print('End of f1')

def f2():
    print("Running 2st thread")
    print("f2 joining f1")
    time.sleep(1)
    t1.join()

    print('f2 sleep')
    time.sleep(2)
    print('End of f2')


if __name__ == '__main__':
    t1 = threading.Thread(target=f1)
    t2 = threading.Thread(target=f2)

    t1.start()
    t2.start()