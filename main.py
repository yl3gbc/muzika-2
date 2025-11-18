import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/home/")
def home():
    return "PR.Andra Solima mūzikas lapa"

@app.get("/notis/")
def notis():
    return ("Notis")

@app.get("/autori/{autori_id}")
def autori(autori_id):
    return f"Autori  {autori_id}"
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)