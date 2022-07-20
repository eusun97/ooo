from fastapi.staticfiles import StaticFiles
from typing import Union, ValuesView
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from fastapi import FastAPI, Request
from pyparsing import html_comment
from fdr_test import prac

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.absolute() / "static"),
    name="static",
)

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root(request: Request):
    return "main page"

@app.get("/trading")
async def root(request: Request):
    print(prac()+"dddddd")
    return templates.TemplateResponse(
        "trading.html", {"request": request, "ooo": prac()}
    )

@app.get("/index")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})