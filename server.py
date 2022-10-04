from pyexpat import model
from fastapi import FastAPI
import uvicorn
from model import *
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

USUARIO = "root"
SENHA = "supermax"
HOST = "35.198.16.4"
BANCO = "formula_one"
PORT = "3306"

CON = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"
engine = create_engine(CON, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Circuits(Base):
    __tablename__ = "circuits"
  
app = FastAPI()


@app.get('')
def mostrarCircuitos():
    return session.query(Circuits).all()
    
@app.get('/drivers')
def Drivers():
    return session.query(drivers).all()
