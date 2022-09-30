from fastapi import FastAPI
from csv.config import *

from csv.config import Session
  
session = Session()
app = FastAPI()

@app.get('/')
def home():
    return session