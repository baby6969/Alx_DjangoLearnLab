from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book


class BookAPITestCase(APITestCase):
    """Unit tests for Book API endpoints"""

    def setUp(self):
        """Set up test data before each test runs"""
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpass")

        # Create an author
        self.author = Author.objects.create(name="J.R.R. Tolkien")

        # Create some books
        self.book1 = Book.objects.create(title="The Hobbit", publication_year=1937, author=self.author)
        self.book2 = Book.objects.create(title="The Lord of the Rings", publication_year=1954, author=self.author)

        # Endpoints
        self.list_url = reverse("book-list")   # should match your urls.py `name`
        self.detail_url = lambda pk: reverse("book-detail", kwargs={"pk": pk})
        self.create_url = reverse("book-create")
        self.update_url = reverse("book-update", kwargs={"pk": self.book1.id})
        self.delete_url = reverse("book-delete", kwargs={"pk": self.book1.id})

    def test_list_books(self):
        """Test retrieving the list of books"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_book_detail(self):
        """Test retrieving a single book by ID"""
        response = self.client.get(self.detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "The Hobbit")

    def test_create_book_authenticated(self):
        """Test creating a new book (must be authenticated)"""
        self.client.login(username="testuser", password="testpass")
        data = {"title": "Silmarillion", "publication_year": 1977, "author": self.author.id}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        """Test creating a book without login (should fail)"""
        data = {"title": "Silmarillion", "publication_year": 1977, "author": self.author.id}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book(self):
        """Test updating a book"""
        self.client.login(username="testuser", password="testpass")
        data = {"title": "The Hobbit - Updated", "publication_year": 1937, "author": self.author.id}
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "The Hobbit - Updated")

    def test_delete_book(self):
        """Test deleting a book"""
        self.client.login(username="testuser", password="testpass")
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_year(self):
        """Test filtering books by publication_year"""
        response = self.client.get(self.list_url + "?publication_year=1937")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "The Hobbit")

    def test_search_books(self):
        """Test searching books by title"""
        response = self.client.get(self.list_url + "?search=Rings")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "The Lord of the Rings")

    def test_order_books_by_year(self):
        """Test ordering books by publication_year descending"""
        response = self.client.get(self.list_url + "?ordering=-publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "The Lord of the Rings")
