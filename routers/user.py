import schema, models
from database import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status,Response,HTTPException
from typing import List
from hashing import Hash
from repository import user


router = APIRouter(
    prefix = '/user',
    tags = ['users'] 
)

@router.post('/',response_model = schema.ShowUser)
def create_user(request:schema.User,db: Session = Depends(get_db)):
    return user.create(request,db)

@router.get('/{id}',status_code = 200,response_model = schema.ShowUser)
def get_user(id:int,db: Session = Depends(get_db)):
    return user.getting_user(id,db)
@router.get("/",response_model = List[schema.ShowUser])
def get_all_user(db: Session = Depends(get_db)):
    return user.getting_all_user(db)