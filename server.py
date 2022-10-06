from model import session, LapTimes, PitStops, Qualifying, Results, SprintResults, Status, ConstructorResults, ConstructorStandings, Constructors, DriverStandings, Races, Circuits, Drivers
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

@app.get("/driver-standings")
def allDriver_standings():
    return session.query(DriverStandings).all()

@app.get("/races")
def allRaces():
    return session.query(Races).all()

@app.get("/pit-stops")
def allPit_stops():
    return session.query(PitStops).all()

@app.get("/qualifying")
def allQualifying():
    return session.query(Qualifying).all()

@app.get("/lap-times")
def allLaps():
    return session.query(LapTimes).all()

@app.get("/results")
def allResults():
    return session.query(Results).all()

@app.get("/sprint-results")
def allSprintResults():
    return session.query(SprintResults).all()

@app.get("/status")
def allStatus():
    return session.query(Status).all()






