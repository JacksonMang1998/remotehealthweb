from flask import Flask,render_template,url_for,request,redirect, make_response
import random
import json
import jsonpickle
from time import time
from random import random
from gpiozero import MCP3008
from pulsesensor import Pulsesensor

app = Flask(__name__)
reading = MCP3008(channel=1)
p =  Pulsesensor()
p.startAsyncBPM()
#new code
@app.route('/', methods=["GET", "POST"])
def welcome():
	return render_template('Welcomepage.html')
@app.route('/signUp', methods=["GET", "POST"])
def signUp():
	return render_template('signup.html') 
@app.route('/login', methods=["GET", "POST"])
def login():
	return render_template('login.html')
#end
@app.route('/main', methods=["GET", "POST"])
def main():
	return render_template('index.html')

@app.route('/data', methods=["GET", "POST"])
def data():
    bpm = p.BPM
    celsius = round((reading.value * 3.3) * 100, 2)
    Temperature = round(celsius * 1.8 + 32, 2) - 65
    Heartbeat = bpm = p.BPM 


    if bpm > 0:
        Heartbeat = p.BPM

    data = [time() * 1000, Temperature, Heartbeat]

    response = make_response(json.dumps(data))
    response.content_type = 'application/json'

    return response


if __name__ == "__main__":
    app.run(debug=True)
 
