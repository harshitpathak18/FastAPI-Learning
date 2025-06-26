import uvicorn
from fastapi import FastAPI, Header
from typing import Optional
from pydantic import BaseModel, Field

# Create the FastAPI instance
app = FastAPI(
    title="📘 FastAPI Demo: Parameters and Headers",
    description="""
    This API demonstrates different types of parameter handling in FastAPI:
    - 📌 Path Parameters
    - ❓ Query Parameters (including optional ones)
    - 📦 Request Body using Pydantic
    - 📭 Request Headers

    Use `/docs` for Swagger UI and `/redoc` for alternative documentation.
    """,
    version="1.0.0",
)



# ----------------------------------------------------------------------------------------------------
@app.get("/", tags=["Root"])
async def read_root() -> dict:
    """
    ✅ Root Endpoint

    - Basic welcome route to test if the API is up.
    - Useful as a health check endpoint.
    """
    return {"message": "Welcome to the FastAPI demo!"}



# ----------------------------------------------------------------------------------------------------
@app.get("/path-parameter/{name}", tags=["Path Parameter"])
async def get_by_path_parameter(name: str) -> dict:
    """
    🔗 Path Parameter

    - Passes parameter **inside** the URL path.
    - Used when the parameter is required and part of resource identification.

    **Usage Example:**
    ```
    GET /path-parameter/harshit
    ```
    """
    return {"message": f"Hello {name}! (from path parameter)"}



# ----------------------------------------------------------------------------------------------------
@app.get("/query-parameter", tags=["Query Parameter"])
async def get_by_query_parameter(name: str) -> dict:
    """
    ❓ Query Parameter

    - Passes parameter in the **query string**.
    - Used when the parameter is optional, filter-like, or not needed to uniquely identify a route.

    **Usage Example:**
    ```
    GET /query-parameter?name=harshit
    ```
    """
    return {"message": f"Hello {name}! (from query parameter)"}



# ----------------------------------------------------------------------------------------------------
@app.get("/path-with-query-parameter/{name}", tags=["Path & Query Parameter"])
async def get_by_path_and_query(name: str, age: int) -> dict:
    """
    🔗📍 Mix of Path and Query Parameters

    - Combines both types in one endpoint.

    **Usage Example:**
    ```
    GET /path-with-query-parameter/harshit?age=23
    ```
    """
    return {"message": f"Name: {name} (path) & Age: {age} (query)"}



# ----------------------------------------------------------------------------------------------------
@app.get("/optional-query-parameter", tags=["Optional Query Parameter"])
async def get_optional_query(
    name: Optional[str] = "Harshit", 
    age: Optional[int] = 0
) -> dict:
    """
    🌀 Optional Query Parameters

    - Can be omitted from the request.
    - If not provided, default values will be used.

    **Usage Examples:**
    ```
    GET /optional-query-parameter
    GET /optional-query-parameter?name=Amit
    GET /optional-query-parameter?name=Neha&age=25
    ```
    """
    return {"message": f"Name: {name} & Age: {age}"}



# ----------------------------------------------------------------------------------------------------
class BookModel(BaseModel):
    book_id: int = Field(..., example=101, description="Unique ID of the book")
    title: str = Field(..., example="Atomic Habits", description="Title of the book")
    author: str = Field(..., example="James Clear", description="Author's name")

@app.post('/create-book', tags=["Request Body With Post"])
async def create_book(book_data: BookModel) -> dict:
    """
    📘 POST Request with JSON Body

    - Accepts a JSON object in the request body using `Pydantic`.

    **Sample JSON Body:**
    ```json
    {
      "book_id": 101,
      "title": "Atomic Habits",
      "author": "James Clear"
    }
    ```

    **Use Case:**
    Useful for creating resources like products, users, posts, etc.
    """
    return {
        "Book Id": book_data.book_id,
        "Title": book_data.title,
        "Author": book_data.author
    }



# ----------------------------------------------------------------------------------------------------
@app.get("/get-headers", status_code=200, tags=["Get All Headers"])
async def get_headers(
    accept: Optional[str] = Header(None),
    content_type: Optional[str] = Header(None),
    user_agent: Optional[str] = Header(None),
    host: Optional[str] = Header(None)
) -> dict:
    """
    📭 Request Headers

    - Extracts common headers from the incoming request.
    - Can be used for analytics, device detection, API versioning, etc.

    **Example Headers Sent by Browser:**
    - Accept: `application/json`
    - Content-Type: `application/json`
    - User-Agent: `Mozilla/...`
    - Host: `127.0.0.1:8000`

    **Usage Example:**
    Use tools like Thunder or cURL to send custom headers.
    """
    return {
        "Accept": accept,
        "Content-Type": content_type,
        "User-Agent": user_agent,
        "Host": host
    }



# ----------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
