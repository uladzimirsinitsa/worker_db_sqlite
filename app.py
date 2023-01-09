from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

from db_connector_sqlite import create_list_urls
from db_connector_sqlite import create_info
from db_connector_sqlite import create_record_db
from db_connector_sqlite import connect
from db_connector_sqlite import update_record_db


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


app = FastAPI()


@app.get("/v1/urls")
async def get_urls():
    return {"urls": create_list_urls()}


@app.post("/v1/info")
async def get_info(request: Info):
    data = jsonable_encoder(request)
    code = data.get("code")
    status = data.get("status")
    return create_info(code, status)


@app.post("/v1/create/record")
async def create_record(request: Record):
    data = jsonable_encoder(request)
    code = data.get("code")
    url = data.get("url")
    status = data.get("status")
    parsing_data = data.get("parsing_data")
    create_record_db(url, status, parsing_data)
    return {"record": "created"}


@app.post("/v1/update/url")
async def update_record(request: Record):
    data = jsonable_encoder(request)
    code = data.get("code")
    url = data.get("url")
    status = data.get("status")
    parsing_data = data.get("parsing_data")
    update_record_db(url, status, parsing_data)
    return {"record": "updated"}
