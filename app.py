from flask import Flask,render_template,request
import os
app = Flask(__name__)

text_fill = os.getenv('TEXT_FILL',default=None)

@app.route('/')
def hostdisplay():
    return render_template('index.html',text_fill=text_fill)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)