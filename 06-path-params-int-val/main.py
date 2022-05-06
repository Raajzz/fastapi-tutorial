from fastapi import FastAPI, Path, Query
from typing import Optional

app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(item_id : Optional[str] = Path(None, min_length=5, max_length=15)):
  item_result = {"item_id":item_id}
  return item_result


@app.get("/arg_order/{item_id}")
async def arg_order(
  *,
  item_id: int = Path(..., title="The ID of the item to get"),
  q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

@app.get("/page/{item_id}")
async def page(
  *,
  item_id: int = Path(..., title="The ID of the item to get", ge = 0, le = 14 ),
  q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

@app.get("/gtle/{item_id}")
async def page(
  *,
  item_id: float = Path(..., title="The ID of the item to get", gt = 0, lt = 14 ),
  q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results