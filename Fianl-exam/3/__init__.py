import smbus
import time
from flask import Flask
from picamera2 import Picamera2

app = Flask(__name__)
picamera = Picamera2()

@app.route('/hello')
def hello():
    ##url 정보

@app.route('led')
def current_led():
    