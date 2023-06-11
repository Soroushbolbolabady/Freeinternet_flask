from flask import Flask
from configmaker import add_client_uuid
app = Flask(__name__)


@app.route("/<uuid>")
def server_config_append(uuid):

    add_client_uuid(uuid)
    return "Everything's fine"
