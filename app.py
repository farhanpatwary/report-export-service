from flask import Flask
import psycopg2
import json
import os

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

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

# Simple routine to run a query on the database and print the results:
def getReports():
    conn = psycopg2.connect('postgres://candidate.suade.org/suade', user=username, password=password)
    cursor = conn.cursor()
    cursor.execute("select * from reports")
    reports = cursor.fetchall()
    print("REPORTS")
    for i in reports:
        print(i)
        element = i[1]
        y = json.loads(element)
        print(y)
    conn.close()

@app.route('/')
def hello():
    getReports()
    return "Hello World!"

if __name__ == '__main__':
    app.run()


