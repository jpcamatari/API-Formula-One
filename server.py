from fastapi import FastAPI
import uvicorn
from model import CON
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

USUARIO = "root"
SENHA = ""
HOST = "localhost"
BANCO = "formula_one"
PORT = "3306"

CON = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"

def conectaBanco():
    engine = create_engine(CON, echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

  
app = FastAPI()

@app.get("/")
def mostrarCircuitos():
    #return session.query(Circuits).all()
    return {'ola':'mundo'}
    
