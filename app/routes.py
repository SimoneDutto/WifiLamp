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
    redc = int(request.args.get("red", ""),16)
    greenc = int(request.args.get("green", ""),16)
    bluec = int(request.args.get("blue", ""),16)
    RGBColor(redc, greenc, bluec) # change color
    return jsonify("OK")



    


