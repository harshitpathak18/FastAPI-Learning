import uvicorn
from typing import List, Optional
from pydantic import BaseModel, Field
from fastapi import FastAPI, HTTPException, status


# -------------------------------------------------------------
# 🚀 FastAPI App Instance
# -------------------------------------------------------------
app = FastAPI(
    title="📘 CRUD Book API",
    description="""
This is a FastAPI application for managing a collection of books.  
You can perform the following operations:

- 📚 View all books  
- ➕ Add a new book  
- 🔍 Get a book by its ID  
- ✏️ Update book details  
- ❌ Delete a book  
""",
    version="1.0.0",
    openapi_tags=[
        {
            "name": "Book",
            "description": "Operations related to book records"
        }
    ]
)


# -------------------------------------------------------------
# 📦 Pydantic Models
# -------------------------------------------------------------
class BookModel(BaseModel):
    book_id: int = Field(..., description="Unique identifier for the book")
    title: str = Field(..., description="Title of the book")
    author: str = Field(..., description="Author of the book")
    page_count: Optional[int] = Field(None, description="Number of pages")
    language: Optional[str] = Field(default="English", description="Language of the book")


class BookUpdateModel(BaseModel):
    title: Optional[str] = Field(None, description="New title (optional)")
    author: Optional[str] = Field(None, description="New author (optional)")
    page_count: Optional[int] = Field(None, description="Updated number of pages (optional)")
    language: Optional[str] = Field(None, description="Updated language (optional)")


# -------------------------------------------------------------
# 📚 In-memory Data Store
# -------------------------------------------------------------
books: List[BookModel] = [
    BookModel(book_id=1, title="Atomic Habits", author="James Clear", page_count=320),
    BookModel(book_id=2, title="Sapiens", author="Yuval Noah Harari", page_count=498),
    BookModel(book_id=3, title="The Alchemist", author="Paulo Coelho", page_count=208, language="Portuguese"),
    BookModel(book_id=4, title="Ikigai", author="Héctor García", page_count=194, language="Japanese"),
    BookModel(book_id=5, title="Zero to One", author="Peter Thiel", page_count=224)
]


# -------------------------------------------------------------
# 📘 Endpoints
# -------------------------------------------------------------

@app.get("/books", response_model=List[BookModel], tags=["Book"])
async def get_all_books():
    """Returns the complete list of books."""
    return books


@app.post("/books", response_model=BookModel, status_code=status.HTTP_201_CREATED, tags=["Book"])
async def create_book(book_data: BookModel):
    """Adds a new book to the collection."""
    if any(book.book_id == book_data.book_id for book in books):
        raise HTTPException(status_code=400, detail="Book with this ID already exists.")
    books.append(book_data)
    return book_data


@app.get("/book/{book_id}", response_model=BookModel, tags=["Book"])
async def get_book(book_id: int):
    """Retrieves a book by its ID."""
    for book in books:
        if book.book_id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.patch("/book/{book_id}", response_model=BookModel, tags=["Book"])
async def update_book(book_id: int, book_update_data: BookUpdateModel):
    """Partially updates an existing book."""
    for book in books:
        if book.book_id == book_id:
            if book_update_data.title is not None:
                book.title = book_update_data.title
            if book_update_data.author is not None:
                book.author = book_update_data.author
            if book_update_data.page_count is not None:
                book.page_count = book_update_data.page_count
            if book_update_data.language is not None:
                book.language = book_update_data.language
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.delete("/book/{book_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Book"])
async def delete_book(book_id: int):
    """Deletes a book by its ID."""
    for book in books:
        if book.book_id == book_id:
            books.remove(book)
            return
    raise HTTPException(status_code=404, detail="Book not found")


# -------------------------------------------------------------
# ▶️ Run with: python main.py
# -------------------------------------------------------------
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
