import pdb
from models.book import Book
from models.author import Author

import repositories.books_repository as books_repository
import repositories.authors_repository as authors_repository

books_repository.delete_all()
authors_repository.delete_all()

author_1 = Author("A", "B")
authors_repository.save(author_1)

author_2 = Author("V", "S")
authors_repository.save(author_2)

authors_repository.select_all()

book_1 = Book("abc", 5)
books_repository.save(book_1)

book_2 = Book("ghj", 5)
books_repository.save(book_2)

book_3 = Book("xyz", 6)
books_repository.save(book_3)

books_repository.select_all()

pdb.set_trace()