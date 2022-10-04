from pyexpat import model
from fastapi import FastAPI
import uvicorn
from model import CON, Circuits, session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

def conectaBanco():
    engine = create_engine(CON, echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

  
app = FastAPI()


@app.get('/')
def mostrarCircuitos():
    return session.query(Circuits).all()
    
