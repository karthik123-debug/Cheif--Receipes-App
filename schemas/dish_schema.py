from pydantic import BaseModel

class DishBase(BaseModel):
    name: str
    type: str | None = None
    chef_id: int

class DishCreate(DishBase):
    pass

class Dish(DishBase):
    id: int

    class Config:
        orm_mode = True
