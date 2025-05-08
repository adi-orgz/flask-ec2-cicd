from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/api/hello')
def hello():
    return {'message': 'Hello from Flask!'}