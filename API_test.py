import logging
import flask
from flask import request
from terra.base_client import Terra

logging.basicConfig(level=logging.INFO)
_LOGGER = logging.getLogger("app")

terra = Terra(api_key='Rtpm90D_hXOyVzG-49iqukoLYLo1gj1u', dev_id='golapicare-testing-hHO3his5ZC', secret="SIGNING-SECRET")

app = flask.Flask(_name_)

@app.route("/consumeTerraWebhook", methods=["POST"])
def consume_terra_webhook() -> flask.Response:
    
    json_data = request.get_json()

    if json_data:
       
        user_id = json_data.get("user", {}).get("user_id")
        webhook_type = json_data.get("type")

     
        _LOGGER.info("Received webhook for user %s of type %s", user_id, webhook_type)

       
        return flask.Response(status=200)
    else:
        
        return flask.Response(status=400, response="Invalid JSON data")

if _name_ == "_main_":
    app.run(host="localhost", port=6969)