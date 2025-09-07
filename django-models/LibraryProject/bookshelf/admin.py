from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns to show
    search_fields = ('title', 'author')                     # Add search box
    list_filter = ('publication_year',)                    # Add filter by year

# Register with custom admin
admin.site.register(Book, BookAdmin)

