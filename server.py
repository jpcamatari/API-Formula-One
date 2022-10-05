from model import CON
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI


# def conectaBanco():
#     engine = create_engine(CON, echo=True)
#     Session = sessionmaker(bind=engine)
#     session = Session()
#     return session

  
app = FastAPI()

@app.get("/")
def root():
    #return session.query(Circuits).all()
    return {'ola':'mundo'}
    
