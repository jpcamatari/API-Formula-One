from sqlite3 import Date
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
    raceId = Column(Integer)
    constructorId = Column(Integer)
    points = Column(Integer)

class ConstructorStandings(Base):
    __tablename__ = "constructor_standings"
    constructorStandingsId = Column(Integer, primary_key=True)
    raceId = Column(String(10))
    constructorId = Column(Integer)
    points = Column(Integer)
    position = Column(Integer)
    positionText = Column(String(10))
    wins = Column(Integer)

class DriverStandings(Base):
    __tablename__ = "driver_standings"
    driverStandingsId = Column(Integer, primary_key=True)
    raceId = Column(String(10))
    driverId = Column(Integer)
    points = Column(Integer)
    position = Column(Integer)
    positionText = Column(String(10))
    wins = Column(Integer)

class Races(Base):
    __tablename__ = "races"
    raceId = Column(Integer, primary_key=True)
    year = Column(String(10))
    round = Column(Integer)
    circuitId = Column(Integer)
    name = Column(String(50))
    data = Column(DateTime)
    wins = Column(Integer)

class PitStops(Base):
    __tablename__ = "pit_stops"
    raceId = Column(Integer, primary_key=True)
    driverId = Column(Integer)
    stop = Column(Integer)
    lap = Column(Integer)
    time = Column(String(50))
    duration = Column(String(50))
    milliseconds = Column(Integer)
  
class Qualifying(Base):
    __tablename__ = "qualifying"
    qualifyId = Column(Integer, primary_key=True)
    raceId = Column(Integer)
    driverId = Column(Integer)
    constructorId = Column(Integer)
    number = Column(Integer)
    position = Column(Integer)
    q1 = Column(String(50))
    q2 = Column(String(50))
    q3 = Column(String(50))

class LapTimes(Base):
    __tablename__ = "lap_times"
    raceId = Column(Integer, primary_key=True)
    driverId = Column(Integer)
    lap = Column(Integer)
    position = Column(Integer)
    time = Column(String(50))
    milliseconds = Column(Integer)

class Results(Base):
    __tablename__ = "results"
    resultId = Column(Integer, primary_key=True)
    raceId = Column(Integer)
    driverId = Column(Integer)
    constructorId = Column(Integer)
    number = Column(Integer)
    grid = Column(Integer)
    position = Column(Integer)
    positionText = Column(String(50))
    positionOrder = Column(String(50))
    points = Column(Integer)
    laps = Column(Integer)
    time = Column(String(50))
    milliseconds = Column(Integer)
    fastestLap = Column(Integer)
    rank = Column(Integer)
    fastestLapTime = Column(String(50))
    fastestLapSpeed = Column(String(50))
    statusId = Column(Integer)

class SprintResults(Base):
    __tablename__ = "sprint_results"
    resultId = Column(Integer, primary_key=True)
    raceId = Column(Integer)
    driverId = Column(Integer)
    constructorId = Column(Integer)
    number = Column(Integer)
    grid = Column(Integer)
    position = Column(Integer)
    positionText = Column(String(50))
    positionOrder = Column(String(50))
    points = Column(Integer)
    laps = Column(Integer)
    time = Column(String(50))
    milliseconds = Column(Integer)
    fastestLap = Column(Integer)
    rank = Column(Integer)
    fastestLapTime = Column(String(50))
    fastestLapSpeed = Column(String(50))
    statusId = Column(Integer)

class Status(Base):
    __tablename__ = "status"
    statusId = Column(Integer, primary_key=True)
    status = Column(String(50))
    


Base.metadata.create_all(engine)

