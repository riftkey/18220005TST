from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):
    name: str
    email: str
    password: str 

class ShowUser(BaseModel):
    name: str
    email: str
    class Config():
        orm_mode = True


class RencanaKuliah(BaseModel):
    semester: int
    jumlah_matakuliah:int
    waktu_belajar_per_hari:int

class ShowRencanaKuliah(BaseModel):
    semester: int
    jumlah_matakuliah:int
    waktu_belajar_per_hari:int
    class Config():
        orm_mode=True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None


class IP(BaseModel):
    ip:float