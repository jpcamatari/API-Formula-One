import pandas as pd
from config import *
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

def retornaSession():
    USUARIO = "root"
    SENHA = ""
    HOST = "localhost"
    BANCO = "formula-one"
    PORT = "3306"

    CON = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"

    engine = create_engine(CON, echo=True)
    Session = sessionmaker(bind=engine)
    return Session()

session = retornaSession()

circuits = pd.read_csv('circuits.csv').split()


# try:
#     for row in circuits:
#         x = Circuits(row)
#         session.add(x)
#         session.commit()
#         print("Executado")
# except Exception as e:
#     print(f'Ocorreu um erro: {e}')

