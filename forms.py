from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Length, Optional

class InternshipFormSubmission(FlaskForm):
    """WTForm class for the internship form.
    
    This form is used to collect and validate internship information from companies.
    It includes fields for company details, contact information, and internship specifics.
    """
    # Company Information
    company_name = StringField('Company Name', validators=[
        DataRequired(), 
        Length(min=2, max=100, message='Company name must be between 2 and 100 characters')
    ])
    company_address = StringField('Company Address', validators=[
        DataRequired(),
        Length(min=5, max=200, message='Address must be between 5 and 200 characters')
    ])
    company_postal_code = StringField('Postal Code', validators=[
        DataRequired(),
        Length(min=2, max=20, message='Postal code must be between 2 and 20 characters')
    ])
    company_city = StringField('City', validators=[
        DataRequired(),
        Length(min=2, max=50, message='City name must be between 2 and 50 characters')
    ])
    
    # Contact Person Information
    contact_name = StringField('Contact Person Name', validators=[
        DataRequired(),
        Length(min=2, max=100, message='Contact name must be between 2 and 100 characters')
    ])
    contact_position = StringField('Position/Role', validators=[
        DataRequired(),
        Length(min=2, max=100, message='Position must be between 2 and 100 characters')
    ])
    contact_email = StringField('Email', validators=[
        DataRequired(),
        Email(message='Please enter a valid email address'),
        Length(max=100, message='Email must be less than 100 characters')
    ])
    contact_phone = StringField('Phone Number', validators=[
        DataRequired(),
        Length(min=8, max=20, message='Phone number must be between 8 and 20 characters')
    ])
    contact_fax = StringField('Fax Number', validators=[
        Optional(),
        Length(max=20, message='Fax number must be less than 20 characters')
    ])
    
    # Internship Details
    internship_title = StringField('Internship Title/Topic', validators=[
        DataRequired(),
        Length(min=5, max=200, message='Title must be between 5 and 200 characters')
    ])
    internship_description = TextAreaField('Internship Description', validators=[
        DataRequired(),
        Length(min=20, message='Please provide a detailed description (minimum 20 characters)')
    ])
    internship_requirements = TextAreaField('Requirements for Interns', validators=[
        Optional()
    ])
    internship_start_date = DateField('Proposed Start Date', format='%Y-%m-%d', validators=[
        Optional()
    ])
    internship_duration = StringField('Expected Duration', validators=[
        Optional(),
        Length(max=50, message='Duration must be less than 50 characters')
    ])
    
    # Confirmation and Submission
    agree_to_terms = BooleanField('I agree that this information can be shared with students', validators=[
        DataRequired(message='You must agree to the terms to submit the form')
    ])
    
    submit = SubmitField('Submit Internship Form') 