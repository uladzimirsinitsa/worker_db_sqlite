
import os
import sqlite3
from dotenv import load_dotenv

load_dotenv()


try:
    DB = os.environ['FILE_DB']
    db = sqlite3.connect(DB)
except KeyError:
    db = sqlite3.connect(r'C:\dbs\test_db.db')


def setup_database():
    CREATE_TABLE = "CREATE TABLE IF NOT EXISTS db_parser(\
                urls STRING PRIMARY KEY, status INT, parsing_data STRING)"
    connect = db.cursor()
    connect.execute(CREATE_TABLE)
    yield connect


def create_list_urls(connect, code, status):
    pass


def _extracted_from_create_info_3(connect, arg0, arg1):
    query = arg0
    data = connect.execute(query)
    return {arg1: len(data.fetchall())}


def create_info(connect, code, status):
    '''Create response'''
    if code == 0:
        return _extracted_from_create_info_3(
            connect,
            "SELECT urls FROM db_parser",
            "all urls"
            )
    if status == 0:
        return _extracted_from_create_info_3(
            connect,
            "SELECT urls FROM db_parser WHERE status=0",
            "all urls status=0"
        )
    if status == 1:
        data = connect.execute("SELECT urls FROM db_parser WHERE status=1")
        return {
            "all urls status=1": len(data.fetchall()),
            }


def create_record(connect, url, status_, parsing_data):
    parameters = (url, status_, parsing_data)
    query = "INSERT OR IGNORE INTO db_parser VALUES (?, ?, ?)"
    connect.execute(query, parameters)
    db.commit()
