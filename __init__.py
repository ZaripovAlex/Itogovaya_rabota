from dotenv import load_dotenv
from os import getenv
load_dotenv('.env.local', '.env')

SOURCE = getenv('SOURCE')
LOGIN = getenv('LOGIN')
PASSWORD = getenv('PASSWORD')