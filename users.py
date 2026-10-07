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

student_1 = Student(1, "Alice", 101, "Computer Science")
teacher_1 = Teacher(2, "Mr. Smith", 201, "Mathematics")

print(student_1.borrow_book("Introduction to Algorithms"))
print(student_1.borrow_book("Data Structures"))
print(student_1.borrow_book("Operating Systems"))
print(student_1.borrow_book("Database Systems"))
print(student_1.return_book("Data Structures"))
print(student_1.borrow_book("Database Systems"))

print(teacher_1.borrow_book("Calculus"))
print(teacher_1.borrow_book("Linear Algebra"))
print(teacher_1.borrow_book("Statistics"))
print(teacher_1.borrow_book("Probability"))