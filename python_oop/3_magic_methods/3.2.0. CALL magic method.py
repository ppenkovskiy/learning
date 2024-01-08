class Counter:
    def __init__(self):
        self.__counter = 0

    def __call__(self, step=1, *args, **kwargs):
        print(f'Starting __call__ magic method for {self}')
        self.__counter += step
        return self.__counter

    def get_counter(self):
        return self.__counter



# CALL magic method is always called when we call functions and classes with '()'
c_1 = Counter()
c_2 = Counter()
c_1()
c_2()
res_1 = c_1(10)
res_2 = c_2(0)
print(res_1, res_2)
