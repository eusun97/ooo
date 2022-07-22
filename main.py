
from ast import Import
from datetime import date
from fastapi.staticfiles import StaticFiles
from typing import Optional, Union, ValuesView
from  fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from fastapi import FastAPI, Request
from h11 import Data
from pyparsing import html_comment

from fdr_test import prac
from topNaver import one_page_list
# from fdr_test import prac
from fdr_testCopy import prac
import sys
sys.path.append("/fdr_testCopy")
import fdr_testCopy as ii
print(ii.currentStock)




from routers import top5_page, detail_page


app = FastAPI()

app.include_router(top5_page.router)
app.include_router(detail_page.router)

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
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/trading")
async def root(request: Request):
    print(prac()+"dddddd")
    return templates.TemplateResponse(
        "trading.html", {"request": request, "ooo": prac()}
    )

    print(one_page_list(1, 1))
    return templates.TemplateResponse(
        "trading.html", {"request": request, "wg": one_page_list(1, 1)}
    )

@app.get("/prac")
async def root(request: Request,q:Optional[str]=ii.currentStock):
    
    
    return templates.TemplateResponse(
        "tradingCopy.html", {"request": request,"q":q, "ooo": prac()}
    )

BASE_DIR = Path(__file__).parent.parent.absolute()

templates = Jinja2Templates(directory=BASE_DIR / "templates")

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

