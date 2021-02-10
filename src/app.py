from flask import Flask, request, abort, jsonify, make_response, render_template
import os
from modules.fileops import add_wisdom, get_random

app = Flask(__name__)

def create_response(status_code, payload):
    rv = dict()
    rv['message'] = payload
    print(rv)
    return make_response(jsonify(rv), status_code)

@app.route("/", methods=['GET'])
def index():
    bullshit = get_random()
    print(type(bullshit))
    return render_template('index.html', retard=bullshit)

@app.route("/upload_wisdom", methods=['GET','POST'])
def upload_wisdom():
    if request.method == 'GET':
        return render_template('upload.html')
    if request.method == 'POST':
        add_wisdom(request.form["wisdom"])
        return render_template('upload.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
