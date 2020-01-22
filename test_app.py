from flask import Flask
from handlers.routes import get_routes

def test_home():
    app = Flask(__name__)
    get_routes(app)
    client = app.test_client()
    url = '/'

    response = client.get(url)
    assert response.status_code == 200

def test_non_existent_report():
    app = Flask(__name__)
    get_routes(app)
    client = app.test_client()
    url = '/100/json'

    response = client.get(url)
    assert response.status_code == 404

def test_report_pdf():
    app = Flask(__name__)
    get_routes(app)
    client = app.test_client()
    url = '/1/pdf'

    response = client.get(url)
    assert response.status_code == 200
    assert response.mimetype == 'application/pdf'

def test_report_xml():
    app = Flask(__name__)
    get_routes(app)
    client = app.test_client()
    url = '/1/xml'

    response = client.get(url)
    assert response.status_code == 200
    assert response.mimetype == 'text/xml'