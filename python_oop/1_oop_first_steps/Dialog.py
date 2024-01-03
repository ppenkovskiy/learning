TYPE_OS = 1


class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


class Dialog:
    obj = None

    def __new__(cls, *args, **kwargs):
        if TYPE_OS == 1:
            obj = super().__new__(DialogWindows)  # creating object of class DialogWindows
        else:
            obj = super().__new__(DialogLinux)  # creating object of class DialogLinux

        obj.name = args[0]
        return obj
