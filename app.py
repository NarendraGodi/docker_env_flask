from flask import Flask,render_template,request
import os
app = Flask(__name__)

name = os.getenv('NAME')
print(name)

@app.route('/')
def webapp():
    return render_template('index.html',name=name)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
