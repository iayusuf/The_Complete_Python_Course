from utils import database_using_sqlite


USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice: """

def menu():
    database_using_sqlite.create_book_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()

        user_input = input(USER_CHOICE)


def prompt_add_book():  # ask for a book name and author
    name = input("Enter the book name: ")
    author = input("Enter the book author: ")
    database_using_sqlite.prompt_add_book(name, author)


def list_books():
    books = database_using_sqlite.get_all_books()
    if not books:
        print("No books to list!")
    for book in books:
        read = 'YES' if book['read'] else 'NO'
        print(f"{book['name']} by {book['author']}, read: {read}")


def prompt_read_book():  # ask for a book name and change it to read in our list

    book_read = input("Enter a book you have read: ")
    print("Great reading! Setting book as read")

    database_using_sqlite.mark_book_as_read(book_read)


def prompt_delete_book():  # ask for book name and remove it from list
    book_to_delete = input("Enter a book to delete: ")

    database_using_sqlite.delete_book(book_to_delete)
    print(f"The book {book_to_delete} has been deleted successfully!")


menu()