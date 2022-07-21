from calendar import prcal
from fastapi import APIRouter, Request
from fastapi.staticfiles import StaticFiles
from typing import Union, ValuesView
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from fastapi import FastAPI, Request
from pyparsing import html_comment
from fdr_test import prac

router = APIRouter()

router.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.parent.absolute() / "static"),
    name="static",
)

BASE_DIR = Path(__file__).parent.parent.absolute()

templates = Jinja2Templates(directory=BASE_DIR / "templates")

@router.get("/trading", response_class=HTMLResponse)
async def root(request: Request):
    print(prac()+"dddddd")
    return templates.TemplateResponse(
        "trading.html", {"request": request, "ooo": prac()}
    )