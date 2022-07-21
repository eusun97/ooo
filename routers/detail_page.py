from calendar import prcal
from fastapi import APIRouter, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from fastapi import FastAPI, Request
from pyparsing import html_comment
import topNaver as tn
from fdr_test import prac

from ast import Import
from datetime import date
from turtle import st

from fastapi.staticfiles import StaticFiles
from typing import List, Optional, Union, ValuesView
from h11 import Data
from pydantic import BaseModel
import sys
sys.path.append("/fdr_test")
import fdr_test as ii
sys.path.append("/topNaver")
import topNaver as tn
from bs4 import BeautifulSoup as bs4

router = APIRouter()

router.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.parent.absolute() / "static"),
    name="static",
)

BASE_DIR = Path(__file__).parent.parent.absolute()

templates = Jinja2Templates(directory=BASE_DIR / "templates")

@router.get("/trading", response_class=HTMLResponse)
async def root(request: Request,q:Optional[str]=ii.currentStock):
    print(prac()+"dddddd")
    return templates.TemplateResponse(
        "trading.html", {"request": request,"q":q, "ooo": prac()}
    )