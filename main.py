1from fastapi import FastAPI
2
3app = FastAPI()
4
5
6@app.get("/")
7async def root():
8    return {"message": "Hello World"}