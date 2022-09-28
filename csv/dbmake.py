import pandas as pd
from config import *
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def retornaSession():
    USUARIO = "root"
    SENHA = "supermax"
    HOST = "35.198.16.4"
    BANCO = "formula_one"
    PORT = "3306"

    CON = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"

    engine = create_engine(CON, echo=True)
    Session = sessionmaker(bind=engine)
    return Session()

session = retornaSession()

lista = ['constructor_results', 'constructor_standings', 'constructors', 'driver_standings', 'pit_stops', 'qualifying', 'races', 'results', 'seasons', 'sprint_results', 'status', 'drivers']

for i in lista:
    df = pd.read_csv(f'csv\{i}.csv', index_col=0)
    df.to_sql(f'{i}', CON)

