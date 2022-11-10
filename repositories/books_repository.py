from db.run_sql import run_sql

from models.author import Author
from models.book import Book

import repositories.books_repository as books_repository
import repositories.authors_repository as authors_repository


def save(book):
    # author = authors_repository(author.id)
    sql = "INSERT INTO books (title, author) VALUES (%s, %s) RETURNING *"
    values = [book.title, book.author_id]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book

def delete_all():
    sql = "DELETE FROM books"
    run_sql(sql)

def select_all():
    books = []

    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        author = authors_repository.select(row['author_id'])
        book = book(row['title'], author, row['id'] )
        books.append(book)
    return books