import threading
import time
import concurrent.futures


class BankAccount:
    def __init__(self):
        self.balance = 100  # shared data/resource
        self.lock_obj = threading.Lock()

    def update(self, transaction, amount):
        print(f"Transaction '{transaction.capitalize()}' started.")

        # self.lock_obj.acquire()
        # tmp_amount = self.balance
        # tmp_amount += amount
        # time.sleep(1)
        # self.balance = tmp_amount
        # self.lock_obj.release()

        with self.lock_obj:  # only 1 thread can enter the code that is protected by threading.Lock()
            tmp_amount = self.balance
            tmp_amount += amount
            time.sleep(1)
            self.balance = tmp_amount

        print(f"Transaction '{transaction.capitalize()}' ended.")


if __name__ == '__main__':
    # lock_obj = threading.Lock()
    # print(lock_obj.locked())
    #
    # lock_obj.acquire()
    # print(lock_obj.locked())
    #
    # lock_obj.release()
    # print(lock_obj.locked())

    acc = BankAccount()
    print(f"Main started. Balance = {acc.balance}.")

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
        ex.map(acc.update, ('refill', 'withdraw'), (100, -200))

    print(f"End of main. Balance = {acc.balance}.")
