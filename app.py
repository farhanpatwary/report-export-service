from flask import Flask, render_template, Response
from modules.reports import getReport
from handlers.routes import get_routes

app = Flask(__name__)
get_routes(app)
if __name__ == '__main__':
    app.run()


