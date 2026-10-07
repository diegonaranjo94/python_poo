class LibraryError(Exception):
    """Base class for other exceptions"""
    pass

class InvalidTitleError(LibraryError):
    """Raised when the title is invalid"""
    pass

class BorrowLimitError(LibraryError):
    """Raised when the user has reached the borrowing limit"""
    pass

class UnavailableBookError(LibraryError):
    """Raised when the book is not available for borrowing"""
    pass

class UserNotFoundError(LibraryError):
    """Raised when the user is not found in the library"""
    pass