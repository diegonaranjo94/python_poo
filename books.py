from dataclasses import dataclass
from typing import Protocol

class BookProtocol(Protocol):
    def borrow(self) -> None:
        """Function implementet in the class that implements this protocol"""
        ...

    def return_book(self) -> None:
        """Function implementet in the class that implements this protocol"""
        ...

    def compute_duration(self) -> int:
        """Function implementet in the class that implements this protocol"""
        ...

class Book:
    def __init__(self, title:str, author:str, isbn:int, available:bool=True):
        self.title: str = title
        self.author:str = author
        self.isbn:int = isbn
        self.available:bool = available
        self.__is_popular: int = 0

    def __str__(self) -> str:
        return f"Book: {self.title} by {self.author}, ISBN: {self.isbn}, Available: {self.available}"

    def borrow(self) -> None:
        if self.available:
            self.available = False
            self.__is_popular += 1
        else:
            return f"{self.title} is currently not available for borrowing."

        return f"{self.title} has been borrowed."

    def return_book(self) -> None:
        if not self.available:
            self.available = True

        return f"{self.title} has been returned."

    def is_popular_book(self) -> bool:
        return self.__is_popular > 5

    def get_borrow_times(self) -> int:
        return self.__is_popular

    def set_borrow_times(self, value:int) -> None:
        self.__is_popular = value


class DigitalBook(Book):
    def duration(self) -> str:
        return '7 days'

class PrintableBook(Book):
    def duration(self) -> str:
        return '14 days'