import json

"""
Concerned with storing and retrieving books from a  json file.
Format of the json file:
This will be stored as a lit of dictionay like below:
[
{
    'name': 'Clean Code',
    'author': 'Robert',
    'read': True
}
]

"""

books_file = 'books.json'

# just to make sure the file is there
def create_book_table():
    with open(books_file, 'w') as file:
        json.dump([], file)

def prompt_add_book(name, author):
    books = get_all_books()
    books.append({'name': name, 'author': author, 'read': False})
    _save_all_books(books)


def get_all_books():
    with open(books_file, 'r') as file:
        return json.load(file)


def _save_all_books(books):
    with open(books_file, 'w') as file:
        return json.dump(books, file)


def mark_book_as_read(book_read):
    books = get_all_books()
    for book in books:
        if book["name"] == book_read:
            book['read'] = True
    _save_all_books(books)


def delete_book(book_to_delete):
    global books_file
    books = get_all_books()
    # The below is a list comprehension to iterate over our books, and only put the book into a new list
    # if the book's name does not match.
    books = [book for book in books if book["name"] != book_to_delete]
    # Here we are calling the below named function which will write the book into the file. We are putting
    # all the books except the book to be deteled i.e. 'book_to_delete'
    _save_all_books(books)