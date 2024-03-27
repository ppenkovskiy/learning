class Handler:
    def __init__(self, methods=('GET',)):
        self.__methods = methods

    def __call__(self, func):
        def wrapper(request, *args, **kwargs):

            method = request.get('method', 'GET')

            if method == 'GET' and 'GET' in self.__methods:
                return self.get(self.__methods, request)
            elif method == 'POST' and 'POST' in self.__methods:
                return self.post(self.__methods, request)
        return wrapper

    def get(self, func, request, *args, **kwargs):
        return f'GET: {func(request)}'

    def post(self, func, request, *args, **kwargs):
        return f'POST: {func(request)}'

    def __getattribute__(self, item):
        # self - link to the instance of the class.
        # print('__getattr__')
        if item == 'x':
            raise ValueError('Access denied')
        else:
            return object.__getattribute__(self, item)

@Handler(methods=('GET', 'POST'))
def contact(request):
    return "Сергей Балакирев"


res = contact({"method": "POST", "url": "contact.html"})
print(res)
