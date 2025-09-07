import django
import os

# Set this to your actual Django project name (the folder with settings.py inside)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")

django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # 1. Query all books by a specific author
    author_name = "J.K. Rowling"
    try:
        author = Author.objects.get(name=author_name)
        books_by_author = author.books.all()
        print(f"Books by {author_name}: {[book.title for book in books_by_author]}")
    except Author.DoesNotExist:
        print(f"No author named {author_name}")

    # 2. List all books in a library
    library_name = "Central Library"
    try:
        library = Library.objects.get(name=library_name)
        books_in_library = library.books.all()
        print(f"Books in {library_name}: {[book.title for book in books_in_library]}")
    except Library.DoesNotExist:
        print(f"No library named {library_name}")

    # 3. Retrieve the librarian for a library
    try:
        librarian = library.librarian
        print(f"Librarian for {library_name}: {librarian.name}")
    except Exception:
        print(f"No librarian assigned to {library_name}")


if __name__ == "__main__":
    run_queries()
