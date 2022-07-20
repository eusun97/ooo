
from fastapi import FastAPI
from topNaver import one_page_list
from fastapi import FastAPI, Request
from typing import Optional

app = FastAPI()

@app.get("/")
def root():
    return{"hello : hi"}

@app.get("/items/{id}/{xyz}")
def item(id:int, xyz:str,q:Optional[str]=None):
    return {"id":id, "q":q,"xyz":xyz}