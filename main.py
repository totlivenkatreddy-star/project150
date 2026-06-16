from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import os

print("CURRENT DIR:", os.getcwd())

app = FastAPI()

# Database / data
students = [{"name": "venkatreddy"}]

# IMPORTANT: make sure engine + Base are imported correctly
Base.metadata.create_all(bind=engine)

# Templates setup
templates = Jinja2Templates(directory="templates")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )