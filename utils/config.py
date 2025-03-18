import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv('BASE_URL')
API_TOKEN = os.getenv('API_TOKEN')