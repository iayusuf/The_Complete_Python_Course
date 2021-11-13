import sqlite3

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


# just to make sure the file is there
def create_book_table():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS books(name txt primary key, author text, read integer)')
    connection.commit()

    connection.close()


def prompt_add_book(name, author):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (name, author))

    connection.commit()
    connection.close()


def get_all_books():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM books')
    books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]

    connection.close()

    return books


def mark_book_as_read(book_read):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('UPDATE books SET read=1 WHERE name=?', (book_read,))
    connection.commit()

    connection.close()


def delete_book(book_to_delete):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('DELETE FROM books WHERE name=?', (book_to_delete,))
    connection.commit()

    connection.close()
