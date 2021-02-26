


class Library(object):
    def __init__(self, signup_time, scan_capacity, books=[]):
        self.books = books
        self.signup_time = signup_time
        self.scan_capacity = scan_capacity

    def add_book(self,book):
        self.books.append(book)
    
    


class Book(object):
    def __init__(self,score=None):
        self.score = score


