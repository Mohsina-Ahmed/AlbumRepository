from lib.book_store import *
"""
When I contruct a book store library
with the fields id, title and author name
They are reflected in the instance properties
"""

def test_contructs_with_fields():
    book_store = Book_Store(1, "Mathematics", "John Leo")
    assert book_store.id == 1
    assert book_store.title == "Mathematics"
    assert book_store.author_name == "John Leo"

'''
When I contruct two book store library with the same fields
They are equal
'''
def test_equality():
    book_store1 = Book_Store(1, 'Nineteen Eighty-Four', 'George Orwell')
    book_store2 = Book_Store(1, 'Nineteen Eighty-Four', 'George Orwell')
    assert book_store1 == book_store2

"""
when I construct a book store 
And I format it to a string
Then it comes out in a friendly format
"""
def test_formatting():
    book_store = Book_Store(1, 'Nineteen Eighty-Four', 'George Orwell')
    assert str(book_store) == "Book_Store(1 - Nineteen Eighty-Four - George Orwell)"