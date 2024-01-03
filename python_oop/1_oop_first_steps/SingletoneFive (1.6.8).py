class SingletonFive:
    __instance = []

    def __new__(cls, name, *args, **kwargs):
        cls.name = name
        if len(cls.__instance) < 5:
            cls.__instance.append(super().__new__(cls))  # creating new object of class DB
        return cls.__instance[-1]

    def __del__(self):
        SingletonFive.__instance = None


objs = [SingletonFive(str(n)) for n in range(10)]
