from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

USUARIO = "root"
SENHA = ""
HOST = "localhost"
BANCO = "formula_one"
PORT = "3306"

CON = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"

engine = create_engine(CON, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Circuits(Base):
    __tablename__ = "circuits"



Base.metadata.create_all(engine)

