from pydantic import BaseModel

class Course(BaseModel):
    title: str
    description: str
    weight: int
    rating: float
    url: str
    image_url: str
    price: float
    source: str

    class Config:
        orm_mode = True
