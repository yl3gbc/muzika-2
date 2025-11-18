import uvicorn
from fastapi import FastAPI

app = FastAPI()

db_immitation =[
    {"id":1, "text":"autori"},
    {"id":2, "text":"autoer1234"},


]

@app.get("/home/")
def home():
    return "PR.Andra Solima mūzikas lapa"

@app.get("/notis/")
def notis():
    return ("Notis")

@app.get("/autori/{autori_id}")
def autori(autori_id):
    if 0 < int(autori_id) <= len(db_immitation):
        return db_immitation[int(autori_id)-1]["text"]
    else:
    return "Ieraksti  nav atyrasti"
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)