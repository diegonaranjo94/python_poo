from users import Student, Teacher, AskProtocol
from books import DigitalBook, PrintableBook
from library import Library
from exceptions import LibraryError, InvalidTitleError, UserNotFoundError

library_1 = Library("Itaka Library")

frankestein = DigitalBook("Frankenstein", "Mary Shelley", 1234567)
hundred_years_of_solitude = PrintableBook("100 Years of Solitude", "Gabriel Garcia Marquez", 2345678)

student_1 = Student(1, "Alice", 101, "Computer Science")
teacher_1 = Teacher(2, "Mr. Smith", 201, "Mathematics")
student_2 = Student(3, "Bob", 102, "Physics")

library_1.users = [student_1, student_2, teacher_1]

library_1.books = [frankestein, hundred_years_of_solitude]

print("Welcome to Itaka Library.")

print("Available books:")
for book in library_1.available_books():
    print(f" - {book}")

user_id = input("Enter user ID to search: ")
try:
    user = library_1.search_user(int(user_id))
    print(f"User found: {user.username}, ID: {user.user_id}")
except UserNotFoundError as e:
    print(f"Error: {e}")