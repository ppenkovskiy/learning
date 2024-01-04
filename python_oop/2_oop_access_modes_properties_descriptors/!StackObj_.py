class StackObj:
    def __init__(self, data=None):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        if type(obj) == StackObj or obj is None:
            self.__next = obj


class Stack:
    def __init__(self):
        self.top = None

    def push(self, obj):
        if self.top is None:
            self.top = obj
        else:
            current_obj = self.top
            while current_obj.next:
                current_obj = current_obj.next
            current_obj.next = obj

    def pop(self):
        if self.top is None:
            return
        if not self.top.next:
            res = self.top
            self.top = None
            return res

        current_obj = self.top
        while current_obj.next.next:
            current_obj = current_obj.next
        res = current_obj.next
        current_obj.next = None
        return res

    def get_data(self):
        if self.top is None:
            return []

        objects_data = []
        current_obj = self.top
        while current_obj:
            objects_data.append(current_obj.data)
            current_obj = current_obj.next
        return objects_data


st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st.pop()
res = st.get_data()  # ['obj1', 'obj2']
print(res)
