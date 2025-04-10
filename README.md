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

## PDF Generation with AcroForm Fields

This project supports two methods of generating filled PDF forms:

1. **AcroForm Filling Method** (Preferred): Directly fills in AcroForm fields within a properly prepared PDF template.
2. **Overlay Method** (Fallback): Overlays text onto a static PDF template.

### Creating a PDF Template with AcroForm Fields

To create a PDF template with proper AcroForm fields:

1. **Use a PDF editing tool** like Adobe Acrobat Pro, PDFescape, or similar tools that support AcroForm creation.
2. **Create form fields** with names matching the field mapping in `pdf_utils.py`:

   - Text fields for strings (company_name, contact_name, etc.)
   - Check boxes for boolean values (wants_meeting, cannot_accept)
   - Date fields for date values

3. **Field naming convention**: Ensure field names in the PDF match those in the field_mapping dictionary:

   ```python
   field_mapping = {
       'company_name': 'company_name',  # Left side is application field, right side is PDF field name
       'company_address': 'company_address',
       # ... more fields
   }
   ```

4. **Save the template** to `static/pdf/template.pdf`

When a properly structured PDF template with AcroForm fields is used, the application will use the direct field filling method, resulting in a cleaner, more accurate PDF output.

### Implementation Details

The system uses the `pdfrw` library to:

1. Read the PDF template and access its form fields
2. Find each field by name and update its value
3. Write the completed PDF to a file

If the template doesn't have AcroForm fields, the system automatically falls back to the overlay method, which renders text on top of the PDF.

## Implementation Changes

### PDF Generation Strategy

We've updated our approach to PDF generation by implementing a dual-strategy system:

1. **AcroForm Field Filling (Primary Method)**

   - Directly fills in existing form fields in the PDF template
   - Provides better accuracy and appearance control
   - Supports text fields and checkboxes
   - Preserves original PDF structure and formatting

2. **Text Overlay Method (Fallback)**
   - Used when the template lacks AcroForm fields
   - Creates a transparent overlay with positioned text
   - Less precise but still functional

### Key Files Modified

- **pdf_utils.py**

  - Added new functions for AcroForm field filling
  - Implemented automatic fallback to the overlay method
  - Enhanced field mapping and data type handling

- **app.py**

  - Updated route handlers to use the new PDF generation method
  - Preserved backward compatibility with existing code

- **test_pdf.py**
  - Added tests for both PDF generation methods
  - Provides verification of the fallback mechanism

### How to Transition to AcroForm Fields

To take full advantage of the new implementation:

1. Create a new PDF template with proper AcroForm fields (as described in the PDF Generation section)
2. Replace the existing template at `static/pdf/template.pdf`
3. No code changes are required - the system will automatically detect and use the AcroForm fields

This implementation significantly improves the accuracy and reliability of the generated PDF forms while maintaining backward compatibility with the existing system.

## Print Layout Optimization

The print layout has been extensively optimized:

- **Form Fits on a Single A4 Page**: All content properly fits on a standard A4 page
- **Improved Typography**: Enhanced heading sizes and font weights
- **Horizontal Contact Rows**: Telephone, telecopie, and email fields display horizontally
- **Student Information Layout**: Nom and Prénoms fields display horizontally
- **Department Table Spacing**: Added proper padding to table cells
- **PDF Preview Removed**: Simplified UI by removing the PDF preview feature
- **Print-Specific Styling**: Added comprehensive print-specific CSS

To use the print feature, simply click the "Imprimer le formulaire" button.
