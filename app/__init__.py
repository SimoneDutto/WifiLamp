from flask import Flask
from flask_ngrok import run_with_ngrok

app = Flask(__name__,template_folder='templates')

from app import routes