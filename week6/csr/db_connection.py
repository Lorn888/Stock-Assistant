import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

host_name = os.environ.get("mysql_host")
database_name = os.environ.get("mysql_db")
user_name = os.environ.get("mysql_user")
user_password = os.environ.get("mysql_pass")

def get_db_connection():
    connection = pymysql.connect(
        host=host_name,
        database=database_name,
        user=user_name,
        password=user_password
    )
    return connection
