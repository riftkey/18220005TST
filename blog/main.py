from fastapi import FastAPI
from . import schemas, models #these . states that it comes from the local directory, namely the same directory this main.py file is in, that is the blog directory. what if we want to import modules from other directory? ig usess u use package? idk
from .database import engine
from .routers import user, authentication, rencanakuliah

app = FastAPI()

app.include_router(user.router)
app.include_router(authentication.router)
app.include_router(rencanakuliah.router)

models.Base.metadata.create_all(engine) #this creates the table in the blog.db file, intinya kalo gk ada ini, gak bakaal kebuat table baru di blog.db
#sidenote: to acccess blog.db you can use tableplus and connect to blog.db









    