import requests
from flask import Flask, jsonify

app = Flask(__name__)

# Terra API configuration
API_URL = 'https://api.tryterra.co/v2/auth/generateWidgetSession'
API_KEY = 'fMcpCMF579LF8fYlFDwLq-EO4o_xpsQ0'
DEV_ID = 'golapicare-staging-RVAcl5Mtck'

def create_widget_session():
    headers = {
        'Accept': 'application/json',
        'dev-id': DEV_ID,
        'content-type': 'application/json',
        'x-api-key': API_KEY
    }
    payload = {
        "providers": "GARMIN,WITHINGS,FITBIT,GOOGLE,TRAININGPEAKS,FREESTYLELIBRE,HUAWEI,POLAR,SUUNTO,EIGHT,APPLE,IFIT",
        "language": "en"
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error during request: {e}")
        return None

@app.route('/')
def index():
    return open('index.html').read()

@app.route('/start-auth', methods=['POST'])
def start_auth():
    response_data = create_widget_session()
    if response_data and 'url' in response_data:
        return jsonify({
            'url': response_data['url'],
            'session_id': response_data.get('session_id', 'N/A')  
        })
    else:
        return jsonify({'error': 'Failed to create widget session'}), 500

if __name__ == '__main__':
    app.run(debug=True)
