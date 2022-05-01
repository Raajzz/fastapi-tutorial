from fastapi import FastAPI
from typing import Optional

app = FastAPI()

# Here, whether we provide anything for limit or not, they'll always exist
@app.get("/items")
async def get_query(skip: int = 0, limit: int = 10):
  return {"skip":skip, "limit":limit}

# But here, if we don't provide q then they'll cease to exist, therefore, depending on q we can conditionally return stuff
@app.get("/items/q")
async def get_optional_query(skip: int = 0, limit: int = 10, q: Optional[str] = None):
  if q:
    return {"skip":skip, "limit":limit, "q":q}
  return {"skip":skip, "limit":limit}

# If you want to make a paramater as required just don't declare anything by default (any value or None) and don't make it to be optional,

# this will cause some error if we neither provide skip or limit or both
@app.get("/items/required")
async def get_query(skip: int = None, limit: int = None):
  return {"skip":skip, "limit":limit}

# Note, if you're using url params then you must provide something there, like it's a must, but query parameters as you know has that special feature that you don't need to provide it.