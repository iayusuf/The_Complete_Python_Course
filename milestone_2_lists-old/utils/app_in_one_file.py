"""
Concerned with storing and retrieving books from a  list
"""

MENU_PROMPT = "\nEnter 'a' to add a book, 'l' to list all books, 'r' to mark a book as read, 'd' to delete a book or " \
              "'q' to quit: "

books = []


def prompt_add_book():  # ask for a book name and author
    name = input("Enter the book name: ")
    author = input("Enter the book author: ")
    books.append({'name': name, 'author': author, 'read': False})


def list_books():
    for book in books:
        print_books(book)


def print_books(book):
    print(f"Name: {book['name']}")
    print(f"Author: {book['author']}")
    print(f"Read: {book['read']}")


def mark_book_as_read():  # ask for a book name and change it to read in our list

    book_read = input("Enter a book you have read: ")
    print("Great reading! Setting book as read")
    for book in books:
        if book["name"] == book_read:
            book['read'] = True


def prompt_delete_book():  # ask for book name and remove it from list

    global books

    print(f"Here are your books so far: {books}")

    book_to_delete = input("Enter a book to delete: ")


    books = [book for book in books if book["name"] != book_to_delete]

    # for book in books:
    #     if book['name'] == book_to_delete:
    #         books.remove(book)

    print(f"The book {book_to_delete} has been removed successfully!")

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice: """


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            mark_book_as_read()
        elif user_input == 'd':
            prompt_delete_book()

        user_input = input(USER_CHOICE)


menu()