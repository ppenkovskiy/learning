class HandlerGET:
    def __init__(self, methods=('GET',)):
        self.__methods = methods

    def __call__(self, request, *args, **kwargs):

        method = request.get('method', 'GET')
        if method == 'GET' and 'GET' in self.__methods:
            return self.get(self.func, request)
        elif method == 'POST' and 'POST' in self.__methods:
            return self.post(self.func, request)
        return None

    def get(self, func, request, *args, **kwargs):
        return f'POST: {func(request)}'

    def post(self, func, request, *args, **kwargs):
        return f'POST: {func(request)}'


@HandlerGET(methods=('GET', 'POST'))
def contact(request):
    return "Сергей Балакирев"


res = contact({"method": "POST", "url": "contact.html"})
print(res)
