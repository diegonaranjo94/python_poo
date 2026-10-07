from typing import Protocol
from exceptions import InvalidTitleError

## Protocols is used to guarantee that an object implements a specific method or set of methods,
## without requiring inheritance from a specific class. This allows for more flexible and decoupled code.
class AskProtocol(Protocol):
    def borrow_book(self, title:str) -> str:
        """Function implementet in the class that implements this protocol"""
        ...

    def return_book(self, title:str) -> str:
        """Function implementet in the class that implements this protocol"""
        ...

class Users:
    def __init__(self, user_id, username, id):
        self.user_id = user_id
        self.username = username
        self.id = id

    def borrow_book(self, title):
        return f"{self.username} has borrowed the book titled '{title}'."

class Student(Users):
    def __init__(self, user_id, username, id, course):
        super().__init__(user_id, username, id)
        self.course = course
        self.book_limit = 3
        self.borrowed_books = []

    def borrow_book(self, title):

        if not title:
            raise InvalidTitleError("Title cannot be empty.")
        
        if len(self.borrowed_books) < self.book_limit:
            self.borrowed_books.append(title)
            return f"{self.username} has borrowed the book titled '{title}'."
        else:
            return f"{self.username} has reached the borrowing limit of {self.book_limit} books."

    def return_book(self, title):
        if title in self.borrowed_books:
            self.borrowed_books.remove(title)
            return f"{self.username} has returned the book titled '{title}'."
        else:
            return f"{self.username} has not borrowed the book titled '{title}'."

class Teacher(Users):
    def __init__(self, user_id, username, id, subject):
        super().__init__(user_id, username, id)
        self.subject = subject
        self.book_limit = None
        self.borrowed_books = []

    def borrow_book(self, title):
        self.borrowed_books.append(title)
        return f"{self.username} has borrowed the book titled '{title}'."

    def return_book(self, title):
        if title in self.borrowed_books:
            self.borrowed_books.remove(title)
            return f"{self.username} has returned the book titled '{title}'."
        else:
            return f"{self.username} has not borrowed the book titled '{title}'."

