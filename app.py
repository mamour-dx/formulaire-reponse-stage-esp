import os
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from config import config_by_name
from models import db, InternshipForm
from forms import InternshipFormSubmission

def create_app(config_name='development'):
    """Factory function to create and configure the Flask application.
    
    Args:
        config_name: The name of the configuration to use (default: 'development')
        
    Returns:
        A configured Flask application instance
    """
    app = Flask(__name__)
    
    # Load configuration from config.py
    app.config.from_object(config_by_name[config_name])
    
    # Initialize extensions with the app
    db.init_app(app)
    
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()
    
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
    @app.route('/')
    def index():
        """Home page route that displays the internship form."""
        form = InternshipFormSubmission()
        return render_template('form.html', form=form, title='Internship Form Submission')
    
    @app.route('/submit', methods=['POST'])
    def submit_form():
        """Handle form submission and save to database."""
        form = InternshipFormSubmission()
        
        if form.validate_on_submit():
            # Create new InternshipForm instance from form data
            internship_form = InternshipForm(
                company_name=form.company_name.data,
                company_address=form.company_address.data,
                company_postal_code=form.company_postal_code.data,
                company_city=form.company_city.data,
                contact_name=form.contact_name.data,
                contact_position=form.contact_position.data,
                contact_email=form.contact_email.data,
                contact_phone=form.contact_phone.data,
                contact_fax=form.contact_fax.data,
                internship_title=form.internship_title.data,
                internship_description=form.internship_description.data,
                internship_requirements=form.internship_requirements.data,
                internship_start_date=form.internship_start_date.data,
                internship_duration=form.internship_duration.data
            )
            
            # Save to database
            db.session.add(internship_form)
            db.session.commit()
            
            flash('Internship form submitted successfully!', 'success')
            return redirect(url_for('form_success', form_id=internship_form.id))
        
        # If form validation fails, return to the form with errors
        flash('Please correct the errors in the form.', 'error')
        return render_template('form.html', form=form, title='Internship Form Submission')
    
    @app.route('/success/<int:form_id>')
    def form_success(form_id):
        """Display success page after form submission."""
        form = InternshipForm.query.get_or_404(form_id)
        return render_template('form_success.html', form=form, title='Submission Successful')
    
    @app.route('/forms')
    def list_forms():
        """Display a list of all submitted internship forms."""
        forms = InternshipForm.query.order_by(InternshipForm.created_at.desc()).all()
        return render_template('list_forms.html', forms=forms, title='Internship Forms')
    
    @app.route('/forms/<int:form_id>')
    def view_form(form_id):
        """Display details of a specific internship form."""
        form = InternshipForm.query.get_or_404(form_id)
        return render_template('view_form.html', form=form, title=f'Internship at {form.company_name}')
    
    @app.errorhandler(404)
    def page_not_found(e):
        """Handle 404 errors."""
        return render_template('404.html', title='Page Not Found'), 404
    
    @app.errorhandler(500)
    def internal_server_error(e):
        """Handle 500 errors."""
        return render_template('500.html', title='Internal Server Error'), 500

if __name__ == '__main__':
    # Get the environment configuration from an environment variable or default to development
    env = os.environ.get('FLASK_ENV', 'development')
    app = create_app(env)
    app.run(host='0.0.0.0', port=5000) 