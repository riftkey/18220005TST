from fastapi import APIRouter, status, Depends, HTTPException
from .. import schemas, database, models
from sqlalchemy.orm import Session
from ..hashing import Hash
from ..repository import user


router = APIRouter(
    prefix='/user',
    tags=['User']
)

@router.post('/', status_code=status.HTTP_201_CREATED,response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    return user.create(request,db)
    

@router.get('/{id}',status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def getUser(id:int, db: Session = Depends(database.get_db)):
    return user.show(id,db)