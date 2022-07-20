# from typing import Union, ValuesView

# from fastapi import FastAPI
# from topNaver import one_page_list


# app = FastAPI()


# @app.get("/")
# def read_root():
#     return {"Hello:World"}

# @app.get("/trading")
# async def one():
    

#     return {"주식 Top 5":one_page_list(1,1)}


from ast import Import
from datetime import date
import enum
from fastapi.staticfiles import StaticFiles
from typing import Optional, Union, ValuesView
from  fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from fastapi import FastAPI, Request
from h11 import Data
from pyparsing import html_comment
from topNaver import one_page_list
# from fdr_test import prac
from fdr_testCopy import prac
from enum import Enum
import sys
sys.path.append("/fdr_testCopy")
import fdr_testCopy as ii
print(ii.currentStock)



app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.parent.absolute() / "static"),
    name="static",
)

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root(request: Request):
    print(one_page_list(1, 1))
    return templates.TemplateResponse(
        "trading.html", {"request": request, "wg": one_page_list(1, 1)}
    )

@app.get("/prac")
async def root(request: Request,q:Optional[str]=ii.currentStock):
    
    
    return templates.TemplateResponse(
        "tradingCopy.html", {"request": request,"q":q, "ooo": prac()}
    )



# class ModelName(str,Enum):
    
#     alexnet=prac()

# @app.get("/user/{model_name}")
# async def datas(model_name: ModelName):
   
#     if model_name == ModelName.alexnet:
#         return {"model_name":model_name, "message": "Deep Deep"}

#     # if model_name.value == "lenet":
#     #     return {"model_name": model_name, "message": "LeCNN all the images"}

#     return {"model_name": model_name, "message": "Have some residuals"}
    

# @app.get("/data")
# async def data(request: Request):
#     from topNaver import one_page_list

#     return one_page_list(1, 1)



# @app.get("/")
# def read_root():
#     return {"Hello:World"}

# @app.get("/trading")
# async def one():
    

#     return {"주식 Top 5":one_page_list(1,1)}

# @app.get("/items/", response_class=HTMLResponse)
# async def read_items():
#     html_content ="""<!DOCTYPE html>
# <html lang="ko">
# <head>
#     <meta charset="UTF-8">
#     <meta http-equiv="X-UA-Compatible" content="IE=edge">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <link rel="stylesheet" href="./css/reset.css">
#     <link rel="stylesheet" href="./css/style.css">
#     <link rel="stylesheet" href="./css/trading.css"> 
#     <title>트리플 이응 - 주식정보</title>
#     <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
#     <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.8.0/chart.min.js"></script>

# </head>
# <body>

#     <header id="header">
#         <div id="header_wrap">
#             <!-- <div id="logo">
#                 <a href="./index.html"><img src="./images/logo.png" alt="트리플이응 로고"></a>
#             </div> -->
#             <!-- //logo -->
#             <div id="search_box">
#                 <form>
#                     <input id="input_search" type="search" placeholder="종목을 입력하세요.">
#                 </form>
#                 <button id="search_btn"></button>
#             </div>
#             <!-- //search_box -->
#         </div>
#         <!-- //header_wrap -->
#     </header>
#     <!-- //header -->
#     <div id="con_wrap" class="con">
#         <h1 id="name">삼성전자</h1>
#         <!-- //name -->
#         <canvas id="line-chart"></canvas>
#         <!-- //chart -->
#         <div id="data"></div>
#         <!-- //data -->
#         <p id="virtual_text">※ 이 페이지는 주식 가상 체험 사이트 입니다. ※ <br>
#             실제 거래를 할 수 없습니다.
#         </p>
#         <!-- //virtual_text -->
#         <div id="trading_box">
#             <ul id="price_wrap">
#                 <li id="price1" class="price">12000</li>
#                 <li id="price2" class="price">12654</li>
#                 <li id="price3" class="price">12450</li>
#             </ul>
#             <span id="trading_text">몇주</span>
#             <div id="trading_btn">
#                 <button id="buy">매수(구매)</button>
#                 <button id="sell">매도(판매)</button>
#             </div>
#         </div>
#          <!--//trading_box  -->
#     </div>
#     <!-- //.con -->
#     <footer id="footer"></footer>

# </body>
# </html>"""
#     return HTMLResponse(content=html_content,status_code=200)

