import random
from werkzeug.routing import BaseConverter
from flask import Flask, jsonify, request, json, session, render_template, redirect, url_for, Response
import run_inference

app = Flask(__name__)

@app.route('/upload')
def upload_temp():
   return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(f.filename)
      message = run_inference.mess(f.filename)
      print(message)
      return Response(message)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == "__main__":
    app.run(host='192.168.43.171',port=8000)
