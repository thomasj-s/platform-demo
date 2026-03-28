from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root_check():
    return "hello world"