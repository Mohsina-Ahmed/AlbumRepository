from lib.book_store import *
class Book_Repository():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM books")
        books = []
        for row in rows:
            book = Book_Store(row["id"], row["title"], row["author_name"])
            books.append(book)
        return books
    
    def find(self, book_id):
        rows = self._connection.execute(
            "SELECT * FROM books WHERE id = %s", [book_id])
        row = rows[0]
        return Book_Store(row['id'], row['title'], row['author_name'])