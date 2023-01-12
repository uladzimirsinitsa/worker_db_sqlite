from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
import json

from db_connector_sqlite import create_list_urls_sqlite
from db_connector_sqlite import create_info_sqlite
from db_connector_sqlite import create_record_db_sqlite
from db_connector_sqlite import update_record_db_sqlite
from db_connector_mysql import create_record_db_mysql
from db_connector_mysql import update_record_db_mysql


class Record(BaseModel):
    '''Request schema'''
    code: int
    url: str
    status: bool
    parsing_data: str


class Info(BaseModel):
    '''Request schema'''
    code: int
    status: int


app = FastAPI()


@app.get("/v1/urls")
async def get_urls():
    return {"urls": create_list_urls_sqlite()}


@app.post("/v1/info")
async def get_info(request: Info):
    data = jsonable_encoder(request)
    code = data.get("code")
    status = data.get("status")
    return create_info_sqlite(code, status)


@app.post("/v1/create/record")
async def create_record(request: Record):
    data = jsonable_encoder(request)
    code = data.get("code")
    url = data.get("url")
    status = data.get("status")
    parsing_data = data.get("parsing_data")
    #  create_record_db_sqlite(url, status, parsing_data)
    create_record_db_mysql(url, status, parsing_data)
    return {"record": "created"}


@app.post("/v1/update/url")
async def update_record(request: Record):
    data = jsonable_encoder(request)
    # code = data.get("code")
    url = data.get("url")
    status = data.get("status")
    parsing_data = data.get("parsing_data")
    #  update_record_db_sqlite(url, status, parsing_data)
    update_record_db_mysql(url, status, parsing_data)
    return {"record": "updated"}
