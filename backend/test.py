
from fastapi import FastAPI
from typing import List, Union
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: Union[str, None] = None


# @app.post("/items/")
# async def create_item(item: Item) -> Item:
#     return item


# @app.get("/items/")
# async def read_items() -> List[Item]:
#     return
item = Item()
