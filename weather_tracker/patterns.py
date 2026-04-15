import psycopg
import os
from dotenv import load_dotenv


load_dotenv()  # Loads variables from .env file

username = os.getenv('db_user')
password = os.getenv('db_pass')

#start here, you got this