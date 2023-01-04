
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

from db_connector import create_list_urls
from db_connector import create_info
from db_connector import create_record


class Record(BaseModel):
    '''Request schema'''
    code_: int
    url: str
    status_: int
    parsing_data: str


class Info(BaseModel):
    '''Request schema'''
    code_: int
    status_: int


class Urls(BaseModel):
    '''Request schema'''
    code_: int
    status_: int


app = FastAPI()


@app.get("/v1/urls")
async def get_urls(request_: Urls):
    data = jsonable_encoder(request_)
    code_ = data.get("code_")
    status_ = data.get("status_")
    return create_list_urls(code_, status_)


@app.get("/v1/info")
async def get_info(request_: Info):
    data = jsonable_encoder(request_)
    code_ = data.get("code_")
    status_ = data.get("status_")
    return create_info(code_, status_)


@app.post("/v1/")
async def root(request_: Record):
    data = jsonable_encoder(request_)
    code_ = data.get("code_")
    url = data.get("url")
    status_ = data.get("status_")
    parsing_data = data.get("parsing_data")
    create_record(url, status_, parsing_data)
    return {"status": "OK"}
