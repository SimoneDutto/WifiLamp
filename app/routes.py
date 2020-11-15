from app import app
from flask import Flask, jsonify, render_template, request
from app.rgb import *

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return render_template('color.html', user=user)

@app.route('/changeColor', methods=["GET"])
def changeColor():
    redc = int(request.args.get("red", ""))
    greenc = int(request.args.get("green", ""))
    bluec = int(request.args.get("blue", ""))
    RGBColor(redc, greenc, bluec) # change color
    return render_template('prova.html')



    


