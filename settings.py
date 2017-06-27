from dotenv import load_dotenv, find_dotenv
import os


load_dotenv(find_dotenv())

OMDB_API_KEY = os.environ.get("OMDB_API_KEY")
OMDB_API_URL = os.environ.get("OMDB_API_URL")
