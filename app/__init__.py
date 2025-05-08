from flask import Flask


def create_app():
    """Application factory function"""
    app = Flask(__name__, template_folder='templates')
    
    # Initialize extensions here (if any)
    
    # Register blueprints or routes
    from app import routes
    app.register_blueprint(routes.bp)
    
    return app