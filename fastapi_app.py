from typing import Union

from fastapi import Body, FastAPI
from pydantic import BaseModel
from typing_extensions import Annotated

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    
    @classmethod
    def __get_pydantic_core_schema__(cls):
        # Generate and return the Pydantic-core schema for the model
        schema = {
            'type': 'object',
            'properties': {
                'name': {'type': 'str'},
                'description': {'type': 'str'},
                'price': {'type': 'float'},
                'tax': {'type': 'float'}
            }
        }
        return schema


@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int,
    item: Annotated[
        Item,
        Body(
            examples=[
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                },
                {
                    "name": "Bar",
                    "price": "35.4",
                },
                {
                    "name": "Baz",
                    "price": "thirty five point four",
                },
            ],
        ),
    ],
):
    results = {"item_id": item_id, "item": item}
    return results