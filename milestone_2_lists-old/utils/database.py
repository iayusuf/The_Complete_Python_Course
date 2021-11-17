"""
Concerned with storing and retrieving books from a  list
"""

books = []


def prompt_add_book(name, author):
    books.append({'name': name, 'author': author, 'read': False})


def get_all_books():
    return books


def mark_book_as_read(book_read):
    for book in books:
        if book["name"] == book_read:
            book['read'] = True


def delete_book(book_to_delete):
    global books
    books = [book for book in books if book["name"] != book_to_delete]
