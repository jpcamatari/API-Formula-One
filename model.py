from typing import Optional
from xmlrpc.client import DateTime
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
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
    circuitId = Column(Integer, primary_key=True)
    circuitRef = Column(String(50))
    name = Column(String(100))
    location = Column(String(100))
    country = Column(String(50))
    lat = Column(Integer)
    lng = Column(Integer)
    alt = Column(Integer)
    url = Column(String(100))

class Drivers(Base):
    __tablename__ = "drivers"
    driverId = Column(Integer, primary_key=True)
    driverRef = Column(String(100))
    number = Column(String(10))
    code = Column(String(10))
    forename = Column(String(100))
    surname = Column(String(100))
    dob = Column(String(50))
    nationality = Column(String(50))

class Constructors(Base):
    __tablename__ = "constructors"
    constructorId = Column(Integer, primary_key=True)
    constructorRef = Column(String(100))
    name = Column(String(100))
    nationality = Column(String(50))

class ConstructorResults(Base):
    __tablename__ = "constructor_results"
    constructorResultsId = Column(Integer, primary_key=True)
    raceId = Column(Integer(10))
    constructorId = Column(Integer(10))
    points = Column(Integer(10))

class ConstructorStandings(Base):
    __tablename__ = "constructor_standings"
    constructorStandingsId = Column(Integer, primary_key=True)
    raceId = Column(String(10))
    constructorId = Column(Integer(10))
    points = Column(Integer(10))
    position = Column(Integer(10))
    positionText = Column(String(10))
    wins = Column(Integer(10))

Base.metadata.create_all(engine)

