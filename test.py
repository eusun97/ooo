from fastapi import FastAPI, File, UploadFile
from fdr_test import prac

app = FastAPI()


@app.post("/files/")
async def create_file(file: bytes = File()):
    return {"file_size": len(file)}


@app.get("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"fdr_test.py": file.filename}