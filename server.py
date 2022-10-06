from model import CON, ConstructorResults, ConstructorStandings, Constructors, session, Circuits, Drivers, Constructor
from fastapi import FastAPI
 
app = FastAPI()

@app.get("/circuits")
def allCircuits():
    return session.query(Circuits).all()

@app.get("/drivers")
def allDrivers():
    return session.query(Drivers).all()

@app.get("/constructors")
def allConstructor():
    return session.query(Constructors).all()

@app.get("/constructor-results")
def allConstructor_results():
    return session.query(ConstructorResults).all()
    
@app.get("/constructor-standings")
def allConstructor_standings():
    return session.query(ConstructorStandings).all()


