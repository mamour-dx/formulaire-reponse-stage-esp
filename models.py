from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize SQLAlchemy instance
db = SQLAlchemy()

class InternshipForm(db.Model):
    """SQLAlchemy model for the internship form submissions.
    
    This model defines the database schema for storing internship form submissions
    with fields for company information, contact details, and internship details.
    """
    __tablename__ = 'internship_forms'
    
    id = db.Column(db.Integer, primary_key=True)
    # Timestamp for submission tracking
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Company Information
    company_name = db.Column(db.String(100), nullable=False)
    company_address = db.Column(db.String(200), nullable=False)
    company_postal_code = db.Column(db.String(20), nullable=False)
    company_city = db.Column(db.String(50), nullable=False)
    
    # Contact Person Information
    contact_name = db.Column(db.String(100), nullable=False)
    contact_position = db.Column(db.String(100), nullable=False)
    contact_email = db.Column(db.String(100), nullable=False)
    contact_phone = db.Column(db.String(20), nullable=False)
    contact_fax = db.Column(db.String(20), nullable=True)
    
    # Internship Details
    internship_title = db.Column(db.String(200), nullable=False)
    internship_description = db.Column(db.Text, nullable=False)
    internship_requirements = db.Column(db.Text, nullable=True)
    internship_start_date = db.Column(db.Date, nullable=True)
    internship_duration = db.Column(db.String(50), nullable=True)
    
    # Status tracking
    is_approved = db.Column(db.Boolean, default=False)
    
    def __repr__(self):
        """String representation of the InternshipForm object."""
        return f'<InternshipForm {self.company_name} - {self.internship_title}>'
    
    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'company_name': self.company_name,
            'company_address': self.company_address,
            'company_postal_code': self.company_postal_code,
            'company_city': self.company_city,
            'contact_name': self.contact_name,
            'contact_position': self.contact_position,
            'contact_email': self.contact_email,
            'contact_phone': self.contact_phone,
            'contact_fax': self.contact_fax,
            'internship_title': self.internship_title,
            'internship_description': self.internship_description,
            'internship_requirements': self.internship_requirements,
            'internship_start_date': self.internship_start_date.isoformat() if self.internship_start_date else None,
            'internship_duration': self.internship_duration,
            'is_approved': self.is_approved
        } 