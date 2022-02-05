import os
from dotenv import load_dotenv
load_dotenv()

# Secret key setting from .env for Flask sessions
SECRET_KEY = os.environ.get('SECRET_KEY')

# DB base configuration from .env for modularity and security reasons
DB = {
    'host': os.environ.get('localhost'),
    'user': os.environ.get('root'),
    'passwd': os.environ.get('Nitay12345'),
    'database': os.environ.get('web-project-g12')
}
