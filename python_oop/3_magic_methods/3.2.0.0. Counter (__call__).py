class Counter:
    def __init__(self):
        self.__counter = 0

    def __call__(self, step=1, *args, **kwargs):
        print('__call__')
        self.__counter += step
        return self.__counter


c_1 = Counter()
c_2 = Counter()
c_1()
c_2(2)
res_1 = c_1(10)
res_2 = c_2(-5)
print(res_1, res_2)
