#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self._page_count = page_count

    def page_count(self):
        return self._page_count

    def set_page_count(self, page_count):
        if not isinstance(page_count, int):
            print("page_count must be an integer")
        else:
            self._page_count = page_count

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    page_count = property(page_count, set_page_count)


book = Book("Oh when the siants", 245)
book.page_count = ''
print(book.page_count)
print(book.turn_page())
