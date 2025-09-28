from django.db import models

# Create your models here.
from django.db import models

class Author(models.Model):
    """
    Author model: Represents a book author.
    Fields:
        - name: The name of the author (string).
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model: Represents a book written by an Author.
    Fields:
        - title: The book title (string).
        - publication_year: Year of publication (integer).
        - author: ForeignKey relationship to Author (many books per author).
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
