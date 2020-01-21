from flask import Flask, Response
from reports import getReports 

app = Flask(__name__)

@app.route('/')
def hello():
    getReports()
    return "Hello World!"

if __name__ == '__main__':
    app.run()


