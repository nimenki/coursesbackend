import uvicorn
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db

from api.v1.schemas.course import Course as SchemaCourse


from models.models import Course as ModelCourse

import os
from dotenv import load_dotenv


load_dotenv('.env')


app = FastAPI()

# to avoid csrftokenError
app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])

@app.get("/")
async def root():
    return {"message": "hello world"}


@app.post('/course/', response_model=SchemaCourse)
async def course(course: SchemaCourse):
    db_book = ModelCourse(
        title=course.title,
        rating=course.rating,
        description = course.description,
        weight = course.weight,
        url = course.url,
        image_url = course.image_url,
        price = course.price,
        source = course.source,
    )
    db.session.add(db_book)
    db.session.commit()
    return db_book

@app.get('/course/')
async def course():
    book = db.session.query(ModelCourse).all()
    return book


# To run locally
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8001)