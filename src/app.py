from flask import Flask, render_template

app = Flask(__name__, template_folder="../templates/", static_folder="../static/")

app.config.from_pyfile("config.py")

from views import *

if  __name__ == "__main__":
    app.run(port=8080, debug=True)