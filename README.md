# Internship Form Portal

A web application built with Flask that allows companies to fill out internship recommendation forms online. The system stores the completed forms in a SQLite database and offers a print-friendly view so that users can easily save or print the form.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup and Installation](#setup-and-installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Deployment](#deployment)
- [Future Enhancements](#future-enhancements)
- [License](#license)
- [Author](#author)

---

## Overview

The Internship Form Portal is designed to simplify the internship recommendation process by replacing non-interactive PDF or image-based forms. Instead, companies can fill out a dynamic web form that is stored in a database and can be printed or saved as a PDF directly from the browser. This project is the first step in a broader initiative that will later include a student portal to review submitted forms.

---

## Features

- **Interactive Internship Form:**  
  Companies can fill out a form with fields like company name, contact person, role, fax number, and proposed internship topic.

- **Form Validation:**  
  Uses client-side (JavaScript) and server-side (Flask) validation to ensure accurate data entry.

- **Print-Friendly and PDF Ready:**  
  Dedicated CSS styling for printing ensures a clean layout. PDF generation can be added using libraries like jsPDF/html2pdf.js for client-side conversion.

- **Data Persistence:**  
  Completed forms are saved in a SQLite database for easy retrieval and later display on a student-facing website.

- **Simple & Extendable:**  
  The codebase is structured to allow rapid development and easy future extensions (e.g., authentication, email notifications).

---

## Tech Stack

- **Backend:**  
  Flask (Python)  
  _Provides an easy-to-use, lightweight framework to build and manage web applications._

- **Database:**  
  SQLite  
  _Ideal for small to medium-sized applications and the easiest to implement in a Flask setup._

- **Frontend:**  
  HTML, CSS, and JavaScript  
  _Uses standard web technologies to create a responsive and interactive user interface._

- **Form Handling:**  
  Flask-WTF (WTForms)  
  _Simplifies form creation and validation._

- **PDF Generation (Optional):**  
  jsPDF / html2pdf.js (client-side integration)  
  _Allows users to generate PDFs from the rendered form._

- **Deployment:**  
  The application is designed to be deployed on a VPS using production servers such as Gunicorn behind an Nginx reverse proxy.

---

## Setup and Installation

### Prerequisites

- Python 3.7 or above
- pip (Python package installer)
- Git (optional, for cloning the repository)

### Step-by-Step Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/internship-form-portal.git
   cd internship-form-portal
   ```
