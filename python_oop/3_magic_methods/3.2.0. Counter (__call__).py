class Counter:
    def __init__(self):
        self.__counter = 0

    def __call__(self, step=1, *args, **kwargs):
        print('__call__')
        self.__counter += step
        return self.__counter


c_1 = Counter()
c_1()
res_1 = c_1(10)
print(res_1)
