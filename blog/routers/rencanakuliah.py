from fastapi import APIRouter, Depends, status, HTTPException
#Library for  get
from typing import List
from sqlalchemy.orm import Session
from .. import schemas,database,models,oauth2 #.. means go up 2 directory
import pickle
import joblib
import sqlite3
import numpy as np

router = APIRouter(
    prefix='/rk',
    tags=['Rencana Kuliah']
)

@router.get('/', status_code=200, response_model=List[schemas.ShowRencanaKuliah])
def get_all_rencanakuliah(db: Session = Depends(database.get_db),current_user:schemas.User = Depends(oauth2.get_current_user)): #need the db again
   allRencanaKuliah = db.query(models.RencanaKuliah).all()
   return allRencanaKuliah

@router.get('/{id}', status_code=200, response_model=schemas.ShowRencanaKuliah) #default status code defined here, response_model is to dictate how your data is returned. to make these response model, go to schemas.py and extend the existing model and put in config, just go to shcemas.py there should be an explanations
def get_rencanakuliah_from_id(id, db: Session = Depends(database.get_db),current_user:schemas.User = Depends(oauth2.get_current_user)): #to get response you need to define response: Response in  here. Response is a module?method? from fastapi
    get_id_filter = db.query(models.RencanaKuliah).filter(models.RencanaKuliah.id == id).first() 
    if not get_id_filter: #if not found
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'rencana kuliah with the id {id} is not available')
    return get_id_filter

@router.post('/', status_code=status.HTTP_201_CREATED) #status_code = status.HTTP_201_CREATED, statusnay itu import dari fastapi
def create_rencanakuliah(request: schemas.RencanaKuliah, db : Session = Depends(database.get_db),current_user:schemas.User = Depends(oauth2.get_current_user)): #request schemas.Blog itu ngetandain request parametersnya harus ngikutin model Pydantic Blog yang ada di file schemas. db = Session = Depends(get_db) itu bukan paramter di interface API docs, melainkan paramater bagi fungsi ini untuk ngefetch si DBnya
    rencanaKuliah = models.RencanaKuliah(semester=request.semester, jumlah_matakuliah=request.jumlah_matakuliah, waktu_belajar_per_hari=request.waktu_belajar_per_hari) #variabel new_blog yang menyimpan nilai berbentuk Blog dari modul models.py  yaitu nilaie title dan body yang didapaktan dari request.title dan request.body
    db.add(rencanaKuliah) #ditamahin ke db , woh berarti db nya gada schema nya? ngikutin si models.Blog aja?
    db.commit() #push ke db (istilahnya kaya add sama commit di git)
    db.refresh(rencanaKuliah) #fetch data yg baru di push?
    return rencanaKuliah #return new rencana_kuliah

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_rencanakuliah(id, db: Session = Depends(database.get_db),current_user:schemas.User = Depends(oauth2.get_current_user)):
    RencanaKuliah = db.query(models.RencanaKuliah).filter(models.RencanaKuliah.id==id)
    if not RencanaKuliah.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'rencana kuliah with id {id} not found')
    db.query(models.RencanaKuliah).filter(models.RencanaKuliah.id==id).delete(synchronize_session=False)
    db.commit()
    return f'rencana kuliah with id {id} has been succesfully deleted'

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_rencanakuliah(request: schemas.RencanaKuliah, id, db: Session = Depends(database.get_db),current_user:schemas.User = Depends(oauth2.get_current_user)):
    db.query(models.RencanaKuliah).filter(models.RencanaKuliah.id == id).update(dict(request),synchronize_session=False)
    db.commit()
    return 'updated successfully'


with open ('gradePrediction.pkl','rb') as f:
    model = pickle.load(f)

@router.post('/gradeprediction',response_model=schemas.IP,status_code=status.HTTP_200_OK)
def predict_ipk(db: Session = Depends(database.get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    connection = sqlite3.connect('blog.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM rencanaKuliah")
    rows = cursor.fetchall()
    for row in rows :
        jumlah_matakuliah = list(row).column.jumlah_matakuliah
        waktu_belajar_per_hari = row.column.waktu_belajar_per_hari
        data_input = np.array([[jumlah_matakuliah,waktu_belajar_per_hari]])
        prediction = model.predict(data_input)
        return {'prediction': int(prediction)}
    
    
    
    
    
    # cursor = database_connect.cursor()
    # cursor.execute('SELECT * FROM rencanaKuliah')
    # rows = cursor.fetchall()
    # for row in rows :
    #     jumlah_matakuliah = row.column.jumlah_matakuliah
    #     waktu_belajar_per_hari = row.column.waktu_belajar_per_hari
    #     data_input = np.array([[jumlah_matakuliah,waktu_belajar_per_hari]])
    #     prediction = model.predict(data_input)
    #     return {'prediction':prediction}

# def something(id, db: Session = Depends(database.get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
#     get_id = db.query(models.RencanaKuliah).filter(models.RencanaKuliah.id==id).first()
#     print(get_id)

# print(something(1,))