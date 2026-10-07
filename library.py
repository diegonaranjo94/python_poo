from exceptions import UserNotFoundError

class Library:
    def __init__(self, name)->None:
        self.name = name
        self.books = []
        self.users = []

    def available_books(self):
        return [book.title for book in self.books if book.available]

    def search_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        raise UserNotFoundError(f"User with ID {user_id} not found.")