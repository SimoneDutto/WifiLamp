from app import app
from flask import Flask, jsonify, render_template, request
import rgb

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return render_template('color.html', user=user)

@app.route('/changeColor', methods=["GET"])
def changeColor():
    redc = request.args.get("red", "")
    greenc = request.args.get("green", "")
    bluec = request.args.get("blue", "")
    rgb.RGBColor(redc, greenc, bluec) # change color
    return render_template('prova.html')



    


