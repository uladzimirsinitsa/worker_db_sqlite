
import os
import sqlite3
from dotenv import load_dotenv

load_dotenv()


try:
    DB = os.environ['FILE_DB']
    db = sqlite3.connect(DB)
except KeyError:
    db = sqlite3.connect(r'C:\dbs\test_db.db')


CREATE_TABLE = "CREATE TABLE IF NOT EXISTS db_parser(\
        urls STRING PRIMARY KEY, status INT, parsing_data STRING)"
c = db.cursor()
c.execute(CREATE_TABLE)


def create_list_urls(code_, status_):
    pass


def create_info(code_, status_):
    '''Create response'''
    if code_ == 0:
        return _extracted_from_create_info_3(
            "SELECT urls FROM db_parser", "all urls"
            )
    if status_ == 0:
        return _extracted_from_create_info_3(
            "SELECT urls FROM db_parser WHERE status=0", "all urls status=0"
        )
    if status_ == 1:
        data = c.execute("SELECT urls FROM db_parser WHERE status=1")
        return {
            "all urls status=1": len(data.fetchall()),
            }


def _extracted_from_create_info_3(arg0, arg1):
    query = arg0
    data = c.execute(query)
    return {arg1: len(data.fetchall())}


def create_record(url, status_, parsing_data):
    parameters = (url, status_, parsing_data)
    query = "INSERT OR IGNORE INTO db_parser VALUES (?, ?, ?)"
    c.execute(query, parameters)
    db.commit()
