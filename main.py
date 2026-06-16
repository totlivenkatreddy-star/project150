from fastapi import FastAPI

app= FastAPI()

@app.get("/")
def home_main():
    return {"welcome":"home"}




