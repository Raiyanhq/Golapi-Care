import logging
import flask
import json
import os
from flask import request
from terra.base_client import Terra

logging.basicConfig(level=logging.INFO)
_LOGGER = logging.getLogger("app")

terra = Terra(api_key='Rtpm90D_hXOyVzG-49iqukoLYLo1gj1u', dev_id='golapicare-testing-hHO3his5ZC', secret="SIGNING-SECRET")

app = flask.Flask(__name__)

# Directory where you want to save the files
jsondump = "Y:\Golapi Care\json_dumpster"
if not os.path.exists(jsondump):
    os.makedirs(jsondump)

@app.route("/consumeTerraWebhook", methods=["POST"])
def consume_terra_webhook() -> flask.Response:
    # Use request.get_json() to get the JSON data from the request
    json_data = request.get_json()

    if json_data:
        # Access specific fields within the JSON data
        user_id = json_data.get("user", {}).get("user_id")
        webhook_type = json_data.get("type")

        # Log the extracted information
        _LOGGER.info("Received webhook for user %s of type %s", user_id, webhook_type)

        # Save the JSON data to a local file
        with open(os.path.join(jsondump, f"webhook_{user_id}_{webhook_type}.json"), 'w') as f:
            json.dump(json_data, f, indent=4)

        # Return a response with a status code of 200
        return flask.Response(status=200, response="JSON data saved successfully")
    else:
        # Return an error response if no valid JSON data is found
        return flask.Response(status=400, response="Invalid JSON data")

if __name__ == "__main__":
    app.run(host="localhost", port=6969)
