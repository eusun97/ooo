from ast import Import
from datetime import date
from turtle import st

from fastapi.staticfiles import StaticFiles
from typing import List, Optional, Union, ValuesView
from  fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from fastapi import FastAPI, Query, Request
from h11 import Data
from pydantic import BaseModel
from pyparsing import html_comment
from fdr_test import prac
from topNaver import STOCK_NAME_LIST, one_page_list
from fdr_testCopy import prac
import sys
sys.path.append("/fdr_testCopy")
import fdr_testCopy as ii
sys.path.append("/topNaver")
import topNaver as tn
from bs4 import BeautifulSoup as bs4


listSt=[]
for names in tn.STOCK_NAME_LIST:
    name=str(names.text) 
    listSt.append(name)


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



@app.get("/index")
async def root(request: Request,q:Optional[list]=listSt):  
    return templates.TemplateResponse(
        "index.html", {"request": request, "q":q})
    

@app.get("/trading")
async def root(request: Request,q:Optional[str]=ii.currentStock):
    print(prac()+"dddddd")
    return templates.TemplateResponse(
        "trading.html", {"request": request,"q":q, "ooo": prac()}
    )


@app.get("/prac")
async def root(request: Request,q:Optional[str]=ii.currentStock):
    return templates.TemplateResponse(
        "tradingCopy.html", {"request": request,"q":q, "ooo": prac()}
    )
