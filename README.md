# Internship Form Portal

A Flask-based web application for companies to fill out, save, print, and submit internship recommendation forms that can later be displayed to students.

## Overview

The Internship Form Portal allows companies to:

- Complete an interactive internship recommendation form online
- Print the form for record keeping
- Submit the form to be stored in a database
- View previously submitted forms

Students can:

- Browse available internship opportunities
- Filter and search for internships by company, title, or description
- View detailed information about each internship

## Tech Stack

- **Backend**: Flask (Python)
- **Database**: SQLite (via SQLAlchemy ORM)
- **Form Handling**: Flask-WTF (WTForms)
- **Frontend**: HTML, CSS, JavaScript
- **Testing**: Pytest

## Features

- Interactive form with validation
- Print-friendly styling for physical copies
- Responsive design for mobile and desktop use
- Searchable internship listings
- Clean, modern UI with accessible design

## Installation and Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation Steps

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/internship-form-portal.git
   cd internship-form-portal
   ```

2. Create and activate a virtual environment:

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables (optional):

   ```
   export FLASK_ENV=development  # On Windows: set FLASK_ENV=development
   export SECRET_KEY=your_secret_key  # For production
   ```

5. Initialize the database:

   ```
   flask shell
   >>> from app import create_app
   >>> from models import db
   >>> app = create_app()
   >>> with app.app_context():
   >>>     db.create_all()
   >>> exit()
   ```

6. Run the application:

   ```
   python app.py
   ```

7. Open your browser and navigate to `http://localhost:5000`

## Project Structure

```
internship-form-portal/
├── app.py                  # Application entry point
├── config.py               # Configuration settings
├── models.py               # Database models
├── forms.py                # Form definitions
├── requirements.txt        # Python dependencies
├── README.md               # This file
├── static/                 # Static assets
│   ├── css/
│   │   └── style.css       # Main stylesheet
│   ├── js/
│   │   └── scripts.js      # Client-side JavaScript
│   └── images/             # Image assets
├── templates/              # HTML templates
│   ├── base.html           # Base template
│   ├── form.html           # Internship form
│   └── list_forms.html     # Form listings
└── tests/                  # Test files
    └── test_app.py         # Application tests
```

## Usage

### For Companies

1. Navigate to the home page to access the internship form
2. Fill out all required fields with your company and internship details
3. Use the "Print Form" button to get a physical copy if needed
4. Submit the form to save it to the database
5. Receive a confirmation with a link to view your submitted form

### For Students

1. Navigate to the "View Forms" page to see all internship opportunities
2. Use the search box to filter by company name, internship title, or description
3. Click on an internship card to view detailed information
4. Use the provided contact information to apply directly to the company

## Development

### Running Tests

```
pytest tests/
```

### Adding New Features

1. Create a new branch: `git checkout -b feature/your-feature-name`
2. Implement your feature
3. Run tests to ensure everything works: `pytest`
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- Flask and its extensions for the excellent web framework
- Contributors and maintainers of the project
