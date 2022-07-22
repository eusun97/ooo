from fastapi import APIRouter, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
from fastapi import  Request
from fastapi.staticfiles import StaticFiles
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
from fastapi import Request
from topNaver import one_page_list
import json


router = APIRouter()

router.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.parent.absolute() / "static"),
    name="static",
)

BASE_DIR = Path(__file__).parent.parent.absolute()

templates = Jinja2Templates(directory=BASE_DIR / "templates")

@router.get("/top5")
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
        "top5.html", {"request": request, "payload":payload})


