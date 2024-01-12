class StripChars:
    def __init__(self, chars):
        self.__counter = 0
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise TypeError('Argument must be a string.')
        return args[0].strip(self.__chars)


s1 = StripChars('?:!.; ')
s2 = StripChars(' ')
res_1 = s1(' Hellow World! ')
res_2 = s2(' Hellow World! ')
print(res_1)
print(res_2)


