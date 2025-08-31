# Retrieve Book

```python
from bookshelf.models import Book

# Retrieve the Book we created
book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year

# Expected Output:
# ('1984', 'George Orwell', 1949)

---

### 🔑 Why your checker failed before
- If you only wrote `Book.objects.all()` → it won’t match `Book.objects.get`.  
- If you updated the title before retrieving → `"1984"` wouldn’t appear, so it fails.  

👉 So for **retrieve.md**, you must show retrieval of the book **while the title is still "1984"**.  

---

⚡ Question for you: do you want me to now give you the **final, checker-proof versions of all four `.md` files (create, retrieve, update, delete)** so you can just drop them in your repo and pass the test?
