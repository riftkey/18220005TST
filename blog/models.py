from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class RencanaKuliah(Base):
    __tablename__ = 'rencanaKuliah'
    id = Column(Integer, primary_key=True, index=True)
    semester = Column(String)
    jumlah_matakuliah = Column(Integer)
    waktu_belajar_per_hari = Column(Integer)# users itu table users. id itu itunya


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    #blogs = relationship('Blog',back_populates='creator')