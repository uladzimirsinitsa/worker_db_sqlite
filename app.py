
import os
import sqlite3
from datetime import datetime

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

DB = os.environ['FILE_DB']


class Record_(BaseModel):
    url: str
    status_: int


app = FastAPI()

db = sqlite3.connect(DB)

create_table = "CREATE TABLE IF NOT EXISTS url_status_db(\
        urls STRING PRIMARY KEY, status INT)"
c = db.cursor()
c.execute(create_table)


def create_record(url, status_):
    parameters = (url, status_)
    query = "INSERT OR IGNORE INTO url_status_db VALUES (?, ?)"
    c.execute(query, parameters)
    db.commit()


@app.post("/")
async def root(record: Record_):
    data = jsonable_encoder(record)
    url = data.get("url")
    status_ = data.get("status_")
    create_record(url, status_)
    return {"status": "OK"}
