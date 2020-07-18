class Book:

    def __init__(self, title, author, num_pages, current_page):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.current_page = current_page
        self.bookmarked_page = 1

    def move_bookmark(self):
        self.bookmarked_page = self.current_page

    def turn_page(self, forward):
        if forward:
            self.current_page += 1
        else:
            self.current_page -= 1

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}"

    def __len__(self):
        return self.num_pages

    def go_directly(self, page):
        self.current_page = page
    def back_first_page(self, back)
        if forward:
            self.current_page += 1

        else:
            self.current_page += 5



book_1 = Book("Cats", "Real Person", 213,1)
print(book_1.current_page)
book_1.turn_page(True)
print(book_1.current_page)
book_1.turn_page(False)
print(book_1.current_page)

book_1.turn_page(True)
book_1.turn_page(True)
book_1.turn_page(True)
book_1.move_bookmark()
book_1.turn_page(True)
print(book_1.current_page, book_1.bookmarked_page)
print(book_1.current_page)
print()
#print(book_1.title)
#print(book_1.author)
#print(book_1.num_pages)

#book_2 = Book("Dogs", "Fake Person", 198, 1)
#print(book_2.title)

#print(book_1)
#print(len(book_1))
