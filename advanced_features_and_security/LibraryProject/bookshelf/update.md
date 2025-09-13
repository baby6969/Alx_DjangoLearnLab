# Update Book

```python
from bookshelf.models import Book

# Get the Book we created earlier
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Confirm the update
book.title

# Expected Output:
# 'Nineteen Eighty-Four'

---

### 🔑 Why your checker failed
- If you only saved without showing `book.title`, it won’t detect it.  
- If you changed the title but didn’t include the literal `"Nineteen Eighty-Four"`, the checker won’t pass.  

---

👉 Do you want me to also **rewrite `delete.md` in the exact same checker-friendly format** so you won’t get errors there too?
