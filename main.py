from fastapi import FastAPI

# init fastapi
app = FastAPI()

# health api
@app.get("/health")
def health_check():
    return {"status": "ok"}

# static data
items = [
    {"item_id": 1, "name": "Item 1"},
    {"item_id": 2, "name": "Item 2"},
    {"item_id": 3, "name": "Item 3"},
]

# get all items
@app.get("/items")
def get_items():
    return items

# get item by id
@app.get("/items/{item_id}")
def get_item_by_id(item_id: int):
    for item in items:
        if item["item_id"] == item_id:
            return item
    return {"message": "Item not found"}

# create item
@app.post("/items")
def create_item(name: str):
    new_item = {"item_id": len(items) + 1, "name": name}
    items.append(new_item)
    return items

