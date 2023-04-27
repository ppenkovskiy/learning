class Viber:
    msgs = []

    @classmethod
    def add_message(cls, msg):
        cls.msgs.append(msg)

    @classmethod
    def remove_message(cls, msg):
        cls.msgs.remove(msg)

    @classmethod
    def set_like(cls, msg):
        if cls.msgs[cls.msgs.index(msg)].fl_like:
            cls.msgs[cls.msgs.index(msg)].fl_like = False
        else:
            cls.msgs[cls.msgs.index(msg)].fl_like = True

    def show_last_message(self, n):
        print(self.msgs[::-1][1:n:])

    @classmethod
    def total_messages(cls):
        return len(cls.msgs)


class Message:
    def __init__(self, text, fl_like=False):
        self.text = text
        self.fl_like = fl_like