from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<html><title>第一个Flask-Web应用</title><h1>Hello World!</h1></html>"