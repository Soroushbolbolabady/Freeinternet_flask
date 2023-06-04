from flask import Flask
from configmaker import add_client_uuid
app = Flask(__name__)


@app.route("/<uuid>")
def hello_world(uuid):

    add_client_uuid(uuid)
    return "Everythings fine"
