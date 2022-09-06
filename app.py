
import os
import sqlite3
from datetime import datetime

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()


DB = os.environ['FILE_DB']

db = sqlite3.connect(DB)

create_query = "create table if not exists url_status_data_db (\
    url, status)"
c = db.cursor()
c.execute(create_query)
db.commit()


class Record(BaseModel):
    url: str
    status: int


def create_record(url, status):
    c.execute(f"INSERT INTO url_status_data_db VALUES(\
        {url}, {status})")
    db.commit()


@app.post("/")
async def root(record: Record):
    dict_ = jsonable_encoder(record)
    url = dict_.get("url")
    status = dict_.get("status")
    create_record(url, status)
    return {"msg": "record create"}
