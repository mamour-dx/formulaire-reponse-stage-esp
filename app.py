import os
from flask import Flask, render_template
from datetime import datetime

from forms import InternshipFormSubmission

def create_app(config_name='development'):
    """Factory function to create and configure the Flask application.
    
    Args:
        config_name: The name of the configuration to use (default: 'development')
        
    Returns:
        A configured Flask application instance
    """
    app = Flask(__name__)
    
    # Set a simple secret key for CSRF protection
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'print-form-tool')
    
    # Register context processors
    @app.context_processor
    def inject_now():
        """Inject the current datetime into templates."""
        return {'now': datetime.utcnow()}
    
    # Register routes
    register_routes(app)
    
    return app

def register_routes(app):
    """Register the application routes with the Flask app.
    
    Args:
        app: The Flask application instance
    """
    @app.route('/', methods=['GET', 'POST'])
    def index():
        """Home page route that displays the internship form for filling and printing."""
        form = InternshipFormSubmission()
        return render_template('form.html', form=form, title='Formulaire de Stage')
    
    @app.errorhandler(404)
    def page_not_found(e):
        """Handle 404 errors."""
        return render_template('404.html', title='Page Non Trouvée'), 404
    
    @app.errorhandler(500)
    def internal_server_error(e):
        """Handle 500 errors."""
        return render_template('500.html', title='Erreur Interne du Serveur'), 500

if __name__ == '__main__':
    # Get the environment configuration from an environment variable or default to development
    env = os.environ.get('FLASK_ENV', 'development')
    app = create_app(env)
    app.run(host='0.0.0.0', port=8080) 