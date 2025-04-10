import os
from flask import Flask, render_template, redirect, url_for, flash, request, send_file, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from config import config_by_name
from models import db, InternshipForm
from forms import InternshipFormSubmission
from pdf_utils import generate_filled_pdf, fill_pdf_form_with_mapping

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
        return render_template('form.html', form=form, title='Formulaire de Stage')
    
    @app.route('/submit', methods=['POST'])
    def submit_form():
        """Handle form submission and save to database."""
        form = InternshipFormSubmission()
        
        if form.validate_on_submit():
            # Create new InternshipForm instance from form data
            internship_form = InternshipForm(
                company_name=form.company_name.data,
                company_address=form.company_address.data,
                contact_phone=form.contact_phone.data,
                contact_fax=form.contact_fax.data,
                contact_email=form.contact_email.data,
                contact_name=form.contact_name.data,
                contact_position=form.contact_position.data,
                contact_phone_direct=form.contact_phone_direct.data,
                contact_fax_direct=form.contact_fax_direct.data,
                contact_email_direct=form.contact_email_direct.data,
                student_name=form.student_name.data,
                student_firstname=form.student_firstname.data,
                internship_positions=form.internship_positions.data,
                internship_topic1=form.internship_topic1.data,
                internship_topic2=form.internship_topic2.data,
                internship_topic3=form.internship_topic3.data,
                wants_meeting=form.wants_meeting.data,
                cannot_accept=form.cannot_accept.data,
                signature_location=form.signature_location.data
            )
            
            # Save to database
            db.session.add(internship_form)
            db.session.commit()
            
            # Generate filled PDF using the submitted form data
            try:
                pdf_path = fill_pdf_form_with_mapping(internship_form)
                # Store the PDF path in the session for later access
                session['last_generated_pdf'] = os.path.basename(pdf_path)
                flash('Formulaire de stage soumis avec succès!', 'success')
            except Exception as e:
                app.logger.error(f"PDF generation error: {str(e)}")
                flash('Formulaire soumis, mais il y a eu un problème lors de la génération du PDF.', 'warning')
            
            return redirect(url_for('form_success', form_id=internship_form.id))
        
        # If form validation fails, return to the form with errors
        flash('Veuillez corriger les erreurs dans le formulaire.', 'error')
        return render_template('form.html', form=form, title='Formulaire de Stage')
    
    @app.route('/success/<int:form_id>')
    def form_success(form_id):
        """Display success page after form submission."""
        form = InternshipForm.query.get_or_404(form_id)
        pdf_filename = session.get('last_generated_pdf', None)
        return render_template('form_success.html', form=form, pdf_filename=pdf_filename, title='Soumission Réussie')
    
    @app.route('/forms')
    def list_forms():
        """Display a list of all submitted internship forms."""
        forms = InternshipForm.query.order_by(InternshipForm.created_at.desc()).all()
        return render_template('list_forms.html', forms=forms, title='Liste des Formulaires')
    
    @app.route('/forms/<int:form_id>')
    def view_form(form_id):
        """Display details of a specific internship form."""
        form = InternshipForm.query.get_or_404(form_id)
        return render_template('view_form.html', form=form, title=f'Stage à {form.company_name}')
    
    @app.route('/download_pdf/<int:form_id>')
    def download_pdf(form_id):
        """Generate and download a filled PDF for a specific form."""
        form = InternshipForm.query.get_or_404(form_id)
        
        try:
            # Generate filled PDF using the form data
            pdf_path = fill_pdf_form_with_mapping(form)
            # Return the PDF as an attachment for download
            return send_file(pdf_path, as_attachment=True, 
                            download_name=f"formulaire_stage_{form.company_name}.pdf")
        except Exception as e:
            app.logger.error(f"PDF download error: {str(e)}")
            flash('Erreur lors de la génération du PDF.', 'error')
            return redirect(url_for('view_form', form_id=form_id))
    
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