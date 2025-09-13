# Django Admin Setup for Book Model

## Steps:

1. Registered `Book` in `bookshelf/admin.py` using:
```python
from .models import Book
from django.contrib import admin

admin.site.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)

admin.site.register(Book, BookAdmin)
