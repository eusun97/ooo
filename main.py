from fastapi.staticfiles import StaticFiles
from typing import Union, ValuesView
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from fastapi import FastAPI, Request
from pyparsing import html_comment
# from fdr_test import prac

from routers import top5_page, detail_page

app = FastAPI()

app.include_router(top5_page.router)
app.include_router(detail_page.router)

app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.absolute() / "static"),
    name="static",
)

BASE_DIR = Path(__file__).parent.parent.absolute()

templates = Jinja2Templates(directory=BASE_DIR / "templates")

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})