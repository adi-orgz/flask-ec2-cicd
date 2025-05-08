from app import app

@app.route('/')
def index():
    return "Flask App Deployed"  # Updated to match test

@app.route('/api/hello')
def hello():
    return {'message': 'Hello from Flask!'}  # Updated to match test