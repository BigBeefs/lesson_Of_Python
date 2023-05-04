from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/comesonobravo")
def home():
    return {"Open": "World"}

@app.get("/input1/{string}")
def nonasynch(string):
    return {"Open": f"World {string}"}


if __name__ == "__main__":
    uvicorn.run("main:app",host="127.0.0.1",port=8000,reload=True)