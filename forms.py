from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, Length, Optional

class InternshipFormSubmission(FlaskForm):
    """WTForm class for the internship form.
    
    This form is used to collect and validate internship information from companies.
    It includes fields to match the official paper form from École Supérieure Polytechnique.
    """
    # Company Information
    company_name = StringField('Entreprise', validators=[
        DataRequired(), 
        Length(min=2, max=100, message='Le nom de l\'entreprise doit être entre 2 et 100 caractères')
    ])
    company_address = StringField('Adresse', validators=[
        DataRequired(),
        Length(min=5, max=200, message='L\'adresse doit être entre 5 et 200 caractères')
    ])
    contact_phone = StringField('Téléphone', validators=[
        DataRequired(),
        Length(min=8, max=20, message='Le numéro de téléphone doit être entre 8 et 20 caractères')
    ])
    contact_fax = StringField('Télécopie', validators=[
        Optional(),
        Length(max=20, message='Le numéro de fax doit être moins de 20 caractères')
    ])
    contact_email = StringField('Email', validators=[
        DataRequired(),
        Email(message='Veuillez entrer une adresse email valide'),
        Length(max=100, message='L\'email doit être moins de 100 caractères')
    ])
    
    # Contact Person Information
    contact_name = StringField('Nom', validators=[
        DataRequired(),
        Length(min=2, max=100, message='Le nom du contact doit être entre 2 et 100 caractères')
    ])
    contact_position = StringField('Fonction', validators=[
        DataRequired(),
        Length(min=2, max=100, message='La fonction doit être entre 2 et 100 caractères')
    ])
    contact_phone_direct = StringField('Téléphone (Direct)', validators=[
        Optional(),
        Length(min=8, max=20, message='Le numéro de téléphone doit être entre 8 et 20 caractères')
    ])
    contact_fax_direct = StringField('Télécopie (Direct)', validators=[
        Optional(),
        Length(max=20, message='Le numéro de fax doit être moins de 20 caractères')
    ])
    contact_email_direct = StringField('Email (Direct)', validators=[
        Optional(),
        Email(message='Veuillez entrer une adresse email valide'),
        Length(max=100, message='L\'email doit être moins de 100 caractères')
    ])
    
    # Student Information (if specific student is assigned)
    student_name = StringField('Nom de l\'étudiant', validators=[
        Optional(),
        Length(max=100, message='Le nom de l\'étudiant doit être moins de 100 caractères')
    ])
    student_firstname = StringField('Prénoms de l\'étudiant', validators=[
        Optional(),
        Length(max=100, message='Les prénoms de l\'étudiant doivent être moins de 100 caractères')
    ])
    
    # Internship Details
    internship_positions = IntegerField('Nombre de positions', validators=[
        Optional()
    ])
    
    # Internship Topics
    internship_topic1 = StringField('Sujet 1', validators=[
        Optional(),
        Length(max=200, message='Le sujet doit être moins de 200 caractères')
    ])
    internship_topic2 = StringField('Sujet 2', validators=[
        Optional(),
        Length(max=200, message='Le sujet doit être moins de 200 caractères')
    ])
    internship_topic3 = StringField('Sujet 3', validators=[
        Optional(),
        Length(max=200, message='Le sujet doit être moins de 200 caractères')
    ])
    
    # Meeting Preferences
    wants_meeting = BooleanField('Souhaite rencontrer un membre du département', validators=[
        Optional()
    ])
    cannot_accept = BooleanField('Ne peut donner suite à la demande', validators=[
        Optional()
    ])
    
    # Signature Information
    signature_location = StringField('Fait à', validators=[
        Optional(),
        Length(max=100, message='L\'emplacement doit être moins de 100 caractères')
    ])
    
    # Submit button
    submit = SubmitField('Soumettre le formulaire') 