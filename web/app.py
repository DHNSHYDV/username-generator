import os
import sys
import json
from flask import Flask, render_template, request, jsonify

# Add the parent directory to the path so we can import the username_generator module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from username_generator import UsernameGenerator

app = Flask(__name__)
generator = UsernameGenerator()

# For Vercel serverless deployment
from serverless_wsgi import handle_request
def handler(event, context):
    return handle_request(app, event, context)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    method = data.get('method', 'adjective_noun')
    with_number = data.get('with_number', True)
    
    usernames = []
    
    if method == 'random':
        length = data.get('length', 8)
        usernames.append(generator.generate_random(length))
    
    elif method == 'adjective_noun':
        usernames.append(generator.generate_adjective_noun(with_number))
    
    elif method == 'themed':
        theme = data.get('theme', 'nature')
        usernames.append(generator.generate_themed(theme, with_number))
    
    elif method == 'name_based':
        name = data.get('name', '')
        if name:
            usernames.append(generator.generate_from_name(name, with_number))
        else:
            return jsonify({'error': 'Name is required for name-based method'}), 400
    
    elif method == 'multiple':
        count = data.get('count', 5)
        theme = data.get('theme')
        
        if theme:
            method_to_use = f"theme_{theme}"
        else:
            method_to_use = "adjective_noun"
            
        try:
            usernames = generator.generate_multiple(count, method_to_use)
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
    
    return jsonify({'usernames': usernames})

if __name__ == '__main__':
    # Use environment port if available (for cloud platforms)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)