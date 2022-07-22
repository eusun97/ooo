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
async def root(request: Request): 

    top_5_list=one_page_list(1,1)
    red=json.loads(top_5_list)

    topNameList=[]
    topCodeList=[]
    for k_name, k_code in zip(red['종목명'], red['code']):
        
        topNameList.append(red['종목명'][k_name])
        topCodeList.append(red['code'][k_code])

    payload={
        "name": topNameList,
        "code": topCodeList,
    }

    return templates.TemplateResponse(
        "index.html", {"request": request, "payload":payload})

@app.get("/trading")
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
        "trading.html", {"request": request, "payload": payload }
    )

@app.get("/prac")
async def root(request: Request,q:Optional[str]=ii.currentStock):
    return templates.TemplateResponse(
        "tradingCopy.html", {"request": request,"q":q, "ooo": prac()}
    )
