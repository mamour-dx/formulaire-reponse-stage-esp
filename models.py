from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize SQLAlchemy instance
db = SQLAlchemy()

class InternshipForm(db.Model):
    """SQLAlchemy model for the internship form submissions.
    
    This model defines the database schema for storing internship form submissions
    with fields matching the official ESP form.
    """
    __tablename__ = 'internship_forms'
    
    id = db.Column(db.Integer, primary_key=True)
    # Timestamp for submission tracking
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Company Information
    company_name = db.Column(db.String(100), nullable=False)
    company_address = db.Column(db.String(200), nullable=False)
    contact_phone = db.Column(db.String(20), nullable=False)
    contact_fax = db.Column(db.String(20), nullable=True)
    contact_email = db.Column(db.String(100), nullable=False)
    
    # Contact Person Information
    contact_name = db.Column(db.String(100), nullable=False)
    contact_position = db.Column(db.String(100), nullable=False)
    contact_phone_direct = db.Column(db.String(20), nullable=True)
    contact_fax_direct = db.Column(db.String(20), nullable=True)
    contact_email_direct = db.Column(db.String(100), nullable=True)
    
    # Student Information (if specific student is assigned)
    student_name = db.Column(db.String(100), nullable=True)
    student_firstname = db.Column(db.String(100), nullable=True)
    
    # Internship Details
    internship_positions = db.Column(db.Integer, nullable=True)
    internship_topic1 = db.Column(db.String(200), nullable=True)
    internship_topic2 = db.Column(db.String(200), nullable=True)
    internship_topic3 = db.Column(db.String(200), nullable=True)
    
    # Meeting Preferences
    wants_meeting = db.Column(db.Boolean, default=False)
    cannot_accept = db.Column(db.Boolean, default=False)
    
    # Signature Information
    signature_location = db.Column(db.String(100), nullable=True)
    
    # Status tracking
    is_approved = db.Column(db.Boolean, default=False)
    
    def __repr__(self):
        """String representation of the InternshipForm object."""
        return f'<InternshipForm {self.company_name} - {self.contact_name}>'
    
    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'company_name': self.company_name,
            'company_address': self.company_address,
            'contact_phone': self.contact_phone,
            'contact_fax': self.contact_fax,
            'contact_email': self.contact_email,
            'contact_name': self.contact_name,
            'contact_position': self.contact_position,
            'contact_phone_direct': self.contact_phone_direct,
            'contact_fax_direct': self.contact_fax_direct,
            'contact_email_direct': self.contact_email_direct,
            'student_name': self.student_name,
            'student_firstname': self.student_firstname,
            'internship_positions': self.internship_positions,
            'internship_topic1': self.internship_topic1,
            'internship_topic2': self.internship_topic2,
            'internship_topic3': self.internship_topic3,
            'wants_meeting': self.wants_meeting,
            'cannot_accept': self.cannot_accept,
            'signature_location': self.signature_location,
            'is_approved': self.is_approved
        } 