
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

from db_connector import create_list_urls
from db_connector import create_info
from db_connector import create_record_db
from db_connector import setup_connection


class Record(BaseModel):
    '''Request schema'''
    code: int
    url: str
    status: int
    parsing_data: str


class Info(BaseModel):
    '''Request schema'''
    code: int
    status: int


class Urls(BaseModel):
    '''Request schema'''
    code: int
    status: int


app = FastAPI()


@app.get("/v1/urls")
async def get_urls(request: Urls):
    data = jsonable_encoder(request)
    code = data.get("code")
    status = data.get("status")
    return create_list_urls(next(setup_connection()), code, status)


@app.get("/v1/info")
async def get_info(request: Info):
    data = jsonable_encoder(request)
    code = data.get("code")
    status = data.get("status")
    return create_info(next(setup_connection()), code, status)


@app.post("/v1/")
async def create_record(request: Record):
    data = jsonable_encoder(request)
    code = data.get("code")
    url = data.get("url")
    status = data.get("status")
    parsing_data = data.get("parsing_data")
    create_record_db(next(setup_connection()), url, status, parsing_data)
    return {"status": "OK"}
