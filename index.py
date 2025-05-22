import os
import sys

# Add the current directory to the path so imports work as expected
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import the Flask app from web/app.py
from web.app import app

# For Vercel serverless deployment
from serverless_wsgi import handle_request

def handler(event, context):
    return handle_request(app, event, context)

# This is used when running locally
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))