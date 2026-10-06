import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

DSN = os.environ.get("DB_NAME")
USN = os.environ.get("USER_NAME")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
PORT = os.environ.get("PORT")
AI_KEY = os.environ.get("AI_KEY")
