
import os
import sqlite3

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from dotenv import load_dotenv


load_dotenv()

DB = os.environ['FILE_DB']


class Record_(BaseModel):
    code_: int
    url: str
    status_: int
    parsing_data: str


class Info_(BaseModel):
    code_: int
    status_: int


class Urls_(BaseModel):
    code_: int
    status_: int


app = FastAPI()

db = sqlite3.connect(DB)

create_table = "CREATE TABLE IF NOT EXISTS db_parser(\
        urls STRING PRIMARY KEY, status INT, parsing_data STRING)"
c = db.cursor()
c.execute(create_table)


def create_list_urls(code_, status_):
    pass


def create_info(code_, status_):
    if code_ == 0:
        query = "SELECT urls FROM db_parser"
        data = c.execute(query)
        return {
            "all urls": len(data.fetchall()),
            }
    if status_ == 0:
        query = "SELECT urls FROM db_parser WHERE status=0"
        data = c.execute(query)
        return {
            "all urls status=0": len(data.fetchall()),
            }
    if status_ == 1:
        query = "SELECT urls FROM db_parser WHERE status=1"
        data = c.execute(query)
        return {
            "all urls status=1": len(data.fetchall()),
            }


def create_record(url, status_, parsing_data):
    parameters = (url, status_, parsing_data)
    query = "INSERT OR IGNORE INTO db_parser VALUES (?, ?, ?)"
    c.execute(query, parameters)
    db.commit()


@app.get("/v1/urls")
async def get_urls(request_: Urls_):
    data = jsonable_encoder(request_)
    code_ = data.get("code_")
    status_ = data.get("status_")
    return create_list_urls(code_, status_)


@app.get("/v1/info")
async def get_info(request_: Info_):
    data = jsonable_encoder(request_)
    code_ = data.get("code_")
    status_ = data.get("status_")
    return create_info(code_, status_)


@app.post("/v1/")
async def root(request_: Record_):
    data = jsonable_encoder(request_)
    code_ = data.get("code_")
    url = data.get("url")
    status_ = data.get("status_")
    parsing_data = data.get("parsing_data")
    create_record(url, status_, parsing_data)
    return {"status": "OK"}
