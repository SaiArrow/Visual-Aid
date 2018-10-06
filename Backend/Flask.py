import os
import random
from werkzeug.routing import BaseConverter
from flask import Flask, jsonify, request, json, session, render_template, redirect, url_for, Response
#import run_inference

app = Flask(__name__)

UPLOAD_FOLDER = os.path.basename("{0}/uploads".format(os.getcwd()))
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/upload')
def upload_temp():
    abs_path = '/home/gurpreet/Documents/Visual-Aid/Backend/uploads'
    if not os.path.exists(abs_path):
        return os.abort(404)
    files = os.listdir(abs_path)
    return render_template('upload.html', files=files)


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['image']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        #message = run_inference.mess(f.filename)     #image sent for testing
        message = "The girl is drinking water in a room | the lady is drinking wine from a bottle | the lady is drinking water in a room"  # dummy caption
        print(message)
        return message


app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
