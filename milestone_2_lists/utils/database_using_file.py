"""
Concerned with storing and retrieving books from a  CSV file.
Format of the CSV file:
name,author,read\n
"""

books_file = 'books.txt'

# just to make sure the file is there
def create_book_table():
    with open(books_file, 'w'):
        pass

def prompt_add_book(name, author):
    with open(books_file, 'a') as file:
        file.write(f'{name},{author},0\n')



def get_all_books():
    with open(books_file, 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]

    return [
        {'name': line[0], 'author': line[1], 'read': line[2]}
        for line in lines
    ]


def mark_book_as_read(book_read):
    books = get_all_books()
    for book in books:
        if book["name"] == book_read:
            book['read'] = '1'
    _save_all_books(books)


def _save_all_books(books):
    with open(books_file, 'w') as file:
        for book in books:
            file.write(f"{book['name']}, {book['author']}, {book['read']}")


def delete_book(book_to_delete):
    global books_file
    books = get_all_books()
    # The below is a list comprehension to iterate over our books, and only put the book into a new list
    # if the book's name does not match.
    books = [book for book in books if book["name"] != book_to_delete]
    # Here we are calling the below named function which will write the book into the file. We are putting
    # all the books except the book to be deteled i.e. 'book_to_delete'
    _save_all_books(books)