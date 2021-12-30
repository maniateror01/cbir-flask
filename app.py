from logging import debug
from flask import Flask, app, render_template

app = Flask(__name__)

@app.route("/")
def Hello_world():
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)