import psycopg2
import json
import os

from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

from dotenv import load_dotenv
load_dotenv()

username = os.getenv("UNAME")
password = os.getenv("PWORD")

# Each row in the reports table looks like this
# { id , OBJECT }
# Where id is the identifier for the row
# and OBJECT is a JSON String
# using json.loads(OBJECT) returns the parsed JSON object
# The returned object is as follows:
# {
#   organization: "ORGANIZATION_NAME",
#   reported_at: REPORTED_AT_DATE,
#   created_at: CREATED_AT_DATE,
#   inventory: [{ name:"ITEM_NAME" , price:ITEM_PRICE },...,{ name:"ITEM_NAME" , price:ITEM_PRICE }]
# }

# Simple routine to run a query on the database and return the report with given ID:
def getReport(id, reportFormat):
    conn = psycopg2.connect('postgres://candidate.suade.org/suade', user=username, password=password)
    cursor = conn.cursor()
    cursor.execute("select * from reports where id="+id)
    report = cursor.fetchall()
    if(cursor.rowcount == 0):
        return "NO RESULTS"
    reportObject = report[0][1]
    reportObjectJSON = json.loads(reportObject)
    conn.close()
    env = Environment(loader=FileSystemLoader('.'))
    template_vars = {
        "reportID" : id,
        "organizationName": reportObjectJSON["organization"],
        "reported_at": reportObjectJSON["reported_at"],
        "created_at": reportObjectJSON["created_at"],
        "inventory": reportObjectJSON["inventory"]
    }
    if(reportFormat == "PDF"):
        template = env.get_template("./templates/reportTemplate.html")
        html_out = template.render(template_vars)
        return HTML(string=html_out).write_pdf()
    elif(reportFormat == "XML"):
        template = env.get_template("./templates/reportTemplate.xml")
        return template.render(template_vars)
    return False
