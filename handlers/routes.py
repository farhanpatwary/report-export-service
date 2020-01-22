from flask import Flask, render_template, Response
from modules.reports import getReport

def get_routes(app):
    @app.route('/')
    def home():
        return render_template("home.html")
        
    @app.route('/<id>/<type>')
    def report(id,type):
        if(type == "xml"):
            result = getReport(id,"XML")
            if(result == "NO RESULTS"):
                return "Report not found", 404
            else:
                return Response(result, mimetype='text/xml')
        else:
            result = getReport(id,"PDF")
            if(result == "NO RESULTS"):
                return "Report not found", 404
            else:
                return Response(result,mimetype = 'application/pdf')
        return "Hello World!"