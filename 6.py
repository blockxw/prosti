from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/time")
def get_time():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"current_time": now}

@app.get("/greet")
def greet(name: str = "stranger"):
    return {"message": f"Hello, {name}!"}
