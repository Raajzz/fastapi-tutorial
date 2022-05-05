from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI()

# Optional[str] means it can be None or it can be string
# Optional[str] is just allow our editor to give us better support
# and detect errors


@app.get("/items")
async def read_itmes(q: Optional[str] = None):
    return {"success": "true", "query params": q}


@app.get("/max")
async def max_items(q: Optional[str] = Query(None, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results["items"].append({"q": q})
    return results


@app.get("/max_min_regex")
async def max_items(
    q: Optional[str] = Query(None, max_length=30, min_length=1, regex="^fixedquery$")
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results["items"].append({"q": q})
    return results


# if nothing is passed then q will have fixedquery
# but if something is gonna be passed then that must satisfy the constraints
# provided in the "Query()" function


@app.get("/default/")
async def read_items(q: str = Query("fixedquery", min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# use of ellipsis ...


@app.get("/ellipses/")
async def read_items(q: str = Query(..., min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# mutiple parameters, Query(None) is needed, don't know why!


@app.get("/items/")
async def read_items(q: Optional[list[str]] = Query(["foo", "bar"])):
    query_items = {"q": q}
    return query_items


# adding meta info
@app.get("/metainfo/")
async def meta_info(
    q: Optional[list[str]] = Query(
        None, title="Query string", description="This is a query string y'all"
    )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# alias

@app.get("/alias/")
async def read_items(q: Optional[str] = Query(None, alias="item-query")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# include_in_schema=False will hide the query from the automatic documentation
# deprecated=True will just notify the automatic documentation that the following 
# parameter is deperecated

@app.get("/exclude/")
async def read_items(
    hidden_query: Optional[str] = Query(None, include_in_schema=True, deprecated=True)
):
    if hidden_query:
        return {"hidden_query": hidden_query}
    else:
        return {"hidden_query": "Not found"}