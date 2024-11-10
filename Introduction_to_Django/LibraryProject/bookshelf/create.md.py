
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from bookshelf.models import Book


book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(f"Book created: {book.title}")

from bookshelf.models import Book


book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(f"Book created: {book.title}")
