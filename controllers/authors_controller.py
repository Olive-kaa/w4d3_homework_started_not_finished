from flask import Flask, render_template
from repositories import authors_repository


# RESTful CRUD Routes

# INDEX
# GET '/authors'
@authors_blueprint.route("/authors")
def authors():
    authors = authors_repository.select_all()
    return render_template("authors/index.html", all_authors = authors)