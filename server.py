from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return "Minha API está no ar"