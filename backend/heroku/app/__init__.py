from flask import Flask
from dotenv import load_dotenv
from os.path import join, dirname
import logging

app = Flask(__name__)

# the .env file is one directory before this
env_path = join(dirname(__file__), '..', '.env')
load_dotenv(env_path)

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)

# import from the package to avoid namespace conflict with app variable
# if you rename the package, there's no need to do this
from app import routes
