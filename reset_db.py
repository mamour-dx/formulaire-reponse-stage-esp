import os
from flask import Flask
from models import db
from config import config_by_name

def reset_database():
    """Drop all tables and recreate them based on current model definitions."""
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(config_by_name['development'])
    
    # Initialize database with app
    db.init_app(app)
    
    with app.app_context():
        print("Dropping all database tables...")
        db.drop_all()
        
        print("Creating all database tables from models...")
        db.create_all()
        
        print("Database reset complete!")

if __name__ == "__main__":
    reset_database() 