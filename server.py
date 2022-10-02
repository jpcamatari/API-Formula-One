from fastapi import FastAPI
from config import *
import uvicorn


from config import Session
  
session = Session()
app = FastAPI()


@app.get('/circuits')
def Circuits():
    return session.query(circuits).all()
    
@app.get('/drivers')
def Drivers():
    return session.query(drivers).all()
    