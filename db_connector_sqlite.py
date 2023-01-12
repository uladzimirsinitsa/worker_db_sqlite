
import os
import sqlite3
from dotenv import load_dotenv

load_dotenv()


# DB_SQLITE = os.environ['FILE_DB_SQLITE']
# db_sqlite = sqlite3.connect(DB_SQLITE)
db_sqlite = sqlite3.connect(r'C:\\dbs\\test_db.db')


CREATE_TABLE = "CREATE TABLE IF NOT EXISTS db_parser(\
            urls STRING PRIMARY KEY, status INT, parsing_data STRING)"
connect = db_sqlite.cursor()
connect.execute(CREATE_TABLE)


def create_list_urls_sqlite():
    query = "SELECT urls FROM db_parser WHERE status=0"
    data = connect.execute(query)
    temp = []
    temp.extend(item[0] for item in data.fetchall())
    return temp


def extracted_from_create_info_sqlite(arg_0, arg_1):
    query = arg_0
    data = connect.execute(query)
    return {arg_1: len(data.fetchall())}


def create_info_sqlite(code, status):
    '''Create info response'''
    if code == 0:
        return extracted_from_create_info_sqlite(
            "SELECT urls FROM db_parser",
            "all urls"
            )
    if status == 0:
        return extracted_from_create_info_sqlite(
            "SELECT urls FROM db_parser WHERE status=0",
            "all urls status=0"
        )
    if status == 1:
        data = connect.execute("SELECT urls FROM db_parser WHERE status=1")
        return {
            "all urls status=1": len(data.fetchall()),
            }


def create_record_db_sqlite(url, status, parsing_data):
    parameters = (url, status, parsing_data)
    query = "INSERT OR IGNORE INTO db_parser VALUES (?, ?, ?)"
    connect.execute(query, parameters)
    db_sqlite.commit()


def update_record_db_sqlite(url, status, parsing_data):
    parameters = (parsing_data, url)
    query = "UPDATE db_parser SET status=1, parsing_data=(?) WHERE urls=(?)"
    connect.execute(query, parameters)
    db_sqlite.commit()
