import requests
from flask import Flask
from flask_cors import CORS
import main
app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    response = main.main()
    #response = "hi"
    # make fancy operations if you want
    return response

if __name__ == "__main__":
    app.run()