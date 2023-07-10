import concurrent.futures
import time
from concurrent.futures import CancelledError


def div(divisor, limit):
    print(f'Started div = {divisor}')

    result = 0
    for x in range(1, limit):
        if x % divisor == 0:
            result += x
            print(f"Divisor = {divisor}, x = {x}")
        time.sleep(0.25)

    print("Raise exception")
    raise Exception('Bad things happen.')
    return result


if __name__ == '__main__':
    print('Started main')
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        res_list = executor.map(div(3, 10), (15, 25))
        while res_list:
            try:
                cur_res = next(res_list)
            except StopIteration:
                print('Stop iteration excepted')
                break
            except Exception as ex:
                print('Generalized exception')
                print(repr(ex))

    print('Main ended')

# if __name__ == '__main__':
#     print('Started main')
#     with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
#         future = executor.submit(div, 3, 15)
#         time.sleep(5)
#         print('Nothing happens until...')
#         try:
#             res = future.result()
#         except CancelledError as ex:
#             print(repr(ex))
#         except TimeoutError as ex:
#             print(repr(ex))
#         except Exception as ex:
#             print(repr(ex))
#     print('Main ended.')
