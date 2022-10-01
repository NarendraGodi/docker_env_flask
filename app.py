from flask import Flask,render_template,request
import os
app = Flask(__name__)

background = os.getenv('BACK_GROUND',default=None)

@app.route('/')
def webapp():
    return render_template('index.html',background=background)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)