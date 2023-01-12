
import os
import mysql.connector

from dotenv import load_dotenv

load_dotenv()


db_mysql = mysql.connector.connect(
    user=os.environ['USER_MYSQL'],
    password=os.environ['PASSWORD_MYSQL'],
    host=os.environ['HOST_MYSQL'],
    database=os.environ['NAME_DATABASE_MYSQL']
    )


connect = db_mysql.cursor()


def update_record_db_mysql(url, status, parsing_data):
    parameters = (status, parsing_data, url)
    query = "UPDATE parser_db_test SET _status=(%s), parsing_data=(%s) WHERE urls=(%s)"
    connect.execute(query, parameters)
    db_mysql.commit()


def create_record_db_mysql(url, status, parsing_data):
    parameters = (url, status, parsing_data)
    query = "INSERT INTO parser_db_test VALUES (%s, %s, %s)"
    connect.execute(query, parameters)
    db_mysql.commit()
