import schema, models
from database import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status,Response,HTTPException
from typing import List
from repository import blog
from routers import oauth2

       
router = APIRouter(
    prefix = '/blog',
    tags = ['blogs']
)

@router.get("/",response_model = List[schema.ShowBlog])
def all(db: Session = Depends(get_db),get_current_user: schema.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)
@router.post('/',status_code = status.HTTP_201_CREATED)
def create(request:schema.Blog, db: Session = Depends(get_db)):
    return blog.create(request,db)
@router.delete('/{id}',status_code= status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db)):
    return blog.delete(id,db)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id,request:schema.Blog, db: Session = Depends(get_db)):
    return blog.update_post(id,request,db)

# @app.get("/blog",response_model = List[ShowBlog],tags=['blogs'])
# def all(db: Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs

@router.get('/{id}',status_code=200,response_model = schema.ShowBlog)
def get_blog_id(id,response: Response,db: Session = Depends(get_db)):
    return blog.get_id(id,response,db)
