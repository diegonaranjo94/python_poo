from dataclasses import dataclass


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

    def get_is_popular(self) -> int:
        return self.__is_popular

    def set_is_popular(self, value:int) -> None:
        self.__is_popular = value


frankestein = Book("Frankenstein", "Mary Shelley", 1234567)


print(frankestein)

frankestein.borrow()
frankestein.return_book()
frankestein.borrow()
frankestein.return_book()
frankestein.borrow()
frankestein.return_book()
frankestein.borrow()
frankestein.return_book()

frankestein.borrow()
frankestein.return_book()
frankestein.borrow()

print(frankestein.is_popular_book())
print(frankestein.get_is_popular())

frankestein.set_is_popular(10)
print(frankestein.get_is_popular())
