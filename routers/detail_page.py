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
from fastapi.staticfiles import StaticFiles
from typing import Optional
from fastapi.templating import Jinja2Templates
from pathlib import Path
from fastapi import FastAPI, Request
from fdr_test import prac
from topNaver import one_page_list
from fdr_testCopy import prac
import sys
sys.path.append("/fdr_testCopy")
import fdr_testCopy as ii
sys.path.append("/topNaver")
import topNaver as tn
import json

router = APIRouter()

router.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.parent.absolute() / "static"),
    name="static",
)

BASE_DIR = Path(__file__).parent.parent.absolute()

templates = Jinja2Templates(directory=BASE_DIR / "templates")

@router.get("/detail")
async def root(
    request: Request, code:Optional[str]=None
):
    top_5_list = one_page_list(1,1)
    res= json.loads(top_5_list)
    bb=[]
    for k_name, k_price, k_code in zip(res['종목명'], res['현재가'], res['code']):
        if(code==res['code'][k_code]):
            bb.append(res['종목명'][k_name])
            bb.append(res['현재가'][k_price])
            bb.append(res['code'][k_code])
            break
    payload = {
        "name": bb[0],
        "close_price": bb[1],
        "price_list": prac(bb[2]),
    }

    return templates.TemplateResponse(
        "detail.html", {"request": request, "payload": payload }
    )