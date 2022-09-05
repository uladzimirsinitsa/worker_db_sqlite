
from fastapi import FastAPI
import sqlite3

app = FastAPI()


FILE_DB = '/data/test_db.db'

db = sqlite3.connect(FILE_DB)

headlines = [
    "url",
    "data",
    "status"
]

create_query = "create table if not exists url_status_data_db (\
    url, data, status)"
c = db.cursor()
c.execute(create_query)
db.commit()


def create_record(url, data, status):
    c.execute(f"INSERT INTO url_status_data_db VALUES(\
        {url}, {data}, {status})")
    db.commit()


@app.get("/")
async def root(url, data, status):
    create_record(url, data, status)
    return {"msg": "record create"}
