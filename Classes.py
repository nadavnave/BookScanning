# Engineer - Nadav Nave

class GoogleBooks(object):
    def __init__(self, B, L, D):
        self.num_of_books   = B
        self.num_libreries  = L
        self.num_of_days    = D
        self.all_books_library = Library(None, None)
        self.libraries = []

class Library(object):
    def __init__(self, signup_time, scan_capacity, books=[]):
        self.books = books
        self.signup_time = signup_time
        self.scan_capacity = scan_capacity

    def add_book(self,book):
        self.books.append(book)

