import os
import secrets

class Config:
    """Base configuration class for the Internship Form Portal application.
    
    Attributes:
        SECRET_KEY: A secret key used for securing the application, particularly for CSRF protection
        SQLALCHEMY_DATABASE_URI: The URI for the SQLite database
        SQLALCHEMY_TRACK_MODIFICATIONS: Disable Flask-SQLAlchemy event system
        DEBUG: Debug mode setting
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or secrets.token_hex(16)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///internship_forms.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False

class DevelopmentConfig(Config):
    """Development configuration settings that extend the base configuration."""
    DEBUG = True
    
class ProductionConfig(Config):
    """Production configuration settings that extend the base configuration."""
    DEBUG = False
    
class TestingConfig(Config):
    """Testing configuration settings for running unit tests."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test_internship_forms.db'
    
# Configuration dictionary to easily select configurations
config_by_name = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}

# Default to development configuration
default_config = config_by_name['development'] 