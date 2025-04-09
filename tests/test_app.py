import os
import pytest
import tempfile
import datetime
from flask import Flask

from app import create_app
from models import db, InternshipForm

class TestConfig:
    """Test configuration."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False
    SECRET_KEY = 'test_secret_key'

@pytest.fixture
def app():
    """Create and configure a Flask app for testing."""
    app = create_app('testing')
    app.config.from_object(TestConfig)
    
    # Create a test client using the Flask application context
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    """Create a test client for the app."""
    return app.test_client()

@pytest.fixture
def runner(app):
    """Create a test CLI runner for the app."""
    return app.test_cli_runner()

def test_home_page(client):
    """Test if the home page loads successfully."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Internship Recommendation Form' in response.data

def test_empty_form_list(client):
    """Test if the form list page loads successfully when empty."""
    response = client.get('/forms')
    assert response.status_code == 200
    assert b'No internship forms have been submitted yet' in response.data

def test_form_submission(client):
    """Test if a form can be submitted successfully."""
    # Create form data
    form_data = {
        'company_name': 'Test Company',
        'company_address': '123 Test Street',
        'company_postal_code': '12345',
        'company_city': 'Test City',
        'contact_name': 'John Doe',
        'contact_position': 'HR Manager',
        'contact_email': 'john.doe@testcompany.com',
        'contact_phone': '123-456-7890',
        'contact_fax': '123-456-7899',
        'internship_title': 'Software Developer Intern',
        'internship_description': 'A detailed description of the internship opportunity.',
        'internship_requirements': 'Knowledge of Python, JavaScript, and web development.',
        'internship_start_date': '2023-06-01',
        'internship_duration': '3 months',
        'agree_to_terms': True
    }
    
    # Submit the form
    response = client.post('/submit', data=form_data, follow_redirects=True)
    
    # Check response
    assert response.status_code == 200
    assert b'Submission Successful' in response.data or b'submitted successfully' in response.data
    
    # Check if form was saved to database
    with client.application.app_context():
        form = InternshipForm.query.filter_by(company_name='Test Company').first()
        assert form is not None
        assert form.contact_email == 'john.doe@testcompany.com'
        assert form.internship_title == 'Software Developer Intern'

def test_invalid_form_submission(client):
    """Test if form validation works correctly for invalid data."""
    # Create invalid form data (missing required fields)
    form_data = {
        'company_name': '',  # Empty required field
        'company_address': '123 Test Street',
        'company_postal_code': '12345',
        'company_city': 'Test City',
        'contact_name': 'John Doe',
        'contact_position': 'HR Manager',
        'contact_email': 'invalid-email',  # Invalid email format
        'contact_phone': '123-456-7890',
        'internship_title': 'Software Developer Intern',
        'internship_description': 'A detailed description.',
        'agree_to_terms': True
    }
    
    # Submit the form
    response = client.post('/submit', data=form_data, follow_redirects=True)
    
    # Check response for validation error message
    assert response.status_code == 200
    assert b'Please correct the errors in the form' in response.data

def test_form_detail_view(client):
    """Test if form detail view works correctly."""
    # First create a form entry in the database
    with client.application.app_context():
        form = InternshipForm(
            company_name='Test Company',
            company_address='123 Test Street',
            company_postal_code='12345',
            company_city='Test City',
            contact_name='John Doe',
            contact_position='HR Manager',
            contact_email='john.doe@testcompany.com',
            contact_phone='123-456-7890',
            internship_title='Software Developer Intern',
            internship_description='A detailed description of the internship opportunity.',
            created_at=datetime.datetime.utcnow()
        )
        db.session.add(form)
        db.session.commit()
        form_id = form.id
    
    # Check if the form view page loads correctly
    response = client.get(f'/forms/{form_id}')
    assert response.status_code == 200
    assert b'Test Company' in response.data
    assert b'Software Developer Intern' in response.data

def test_nonexistent_form_view(client):
    """Test if trying to view a nonexistent form returns 404."""
    response = client.get('/forms/999')  # Assuming ID 999 doesn't exist
    assert response.status_code == 404 