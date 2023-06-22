import math


class Pagination:

    def __init__(self, items=[], page_size=10, current_page=1):
        self.items = items
        self.page_size = page_size
        self.current_page = current_page
        self.last_page_ = math.ceil(len(self.items) / self.page_size)

    def get_visible_items(self):
        return self.items[(self.current_page - 1) * self.page_size: self.current_page * self.page_size]

    def prev_page(self):
        if self.current_page > 1:
            self.current_page -= 1
        print(self.get_visible_items())

    def next_page(self):
        if self.current_page < self.last_page_:
            self.current_page += 1
        return self.get_visible_items()

    def first_page(self):
        self.current_page = 1
        return  self.get_visible_items()

    def last_page(self):
        self.current_page = self.last_page_
        return self.get_visible_items()

    def go_to_page(self, page):
        if page < 1:
            self.current_page = 1
        elif page > self.last_page_:
            self.current_page = self.last_page_
        else:
            self.current_page = page
        return self.get_visible_items()

    def get_current_page(self):
        return self.current_page

    def get_page_size(self):
        return len(self.items[(self.current_page - 1) * self.page_size: self.current_page * self.page_size])

    def get_items(self):
        return self.items


p = Pagination(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'], 3)
print(p.next_page().next_page())