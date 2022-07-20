from fastapi.staticfiles import StaticFiles
from typing import Union, ValuesView
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from fastapi import FastAPI, Request
from pyparsing import html_comment
from fdr_test import prac
from fastapi import APIRouter

router = APIRouter

router.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.parent.absolute() / "static"),
    name="static",
)

templates = Jinja2Templates(directory="../templates")

@router.get("/index")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})