class Viber:
    msgs = []

    @classmethod
    def add_message(cls, msg):
        cls.msgs.append(msg)

    def remove_message(self, msg):
        self.msgs.remove(msg)

    def set_like(self, msg):
        if self.msgs[self.msgs.index(msg)].fl_like:
            self.msgs[self.msgs.index(msg)].fl_like = False
        else:
            self.msgs[self.msgs.index(msg)].fl_like = True

    def show_last_message(self, n):
        print(self.msgs[::-1][1:n:])

    def total_messages(self):
        return len(self.msgs)


class Message:
    def __init__(self, text, fl_like=False):
        self.text = text
        self.fl_like = fl_like


msg_1 = Message("Hi")
msg_2 = Message("Ho")
Viber.add_message(msg_1)
Viber.add_message(msg_2)
print(len(Viber.msgs))
