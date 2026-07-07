# Secure Student Management System

## Project Overview

This project is a **Secure Software Design and Development** web application built with Flask. It provides a simple admin-controlled Student Management System for adding, viewing, editing, and deleting student records.

The final repository keeps all application code inside the `src/` directory and removes unsafe development artifacts such as `.env`, `env/`, `.git/`, `__pycache__/`, and database files.

## Team Members

| Name |
|---|
| Syed Jazib Ali Rizvi |
| Hussain Ali |

## Technology Stack

| Component | Technology |
|---|---|
| Backend | Flask |
| Database ORM | Flask-SQLAlchemy |
| Forms and validation | Flask-WTF / WTForms |
| Database | SQLite |
| UI | Bootstrap |
| Local assets | `src/static/img/aulogo.png` for navbar logo |
| Containerization | Docker |

## Repository Structure

```text
secure-student-management-system/
|-- src/
|   |-- app.py
|   |-- forms.py
|   |-- create_db.py
|   |-- templates/
|   |   |-- dashboard.html
|   |   |-- index.html
|   |   |-- login.html
|   |   |-- register.html
|   |   `-- update.html
|   `-- static/
|-- docs/
|   |-- secure-student-management-system-report.docx
|   `-- secure-student-management-system-report.pdf
|-- screenshots/
|-- requirements.txt
|-- Dockerfile
|-- .dockerignore
|-- .env.example
|-- README.md
|-- PROJECT_NOTES.md
|-- RUN_GUIDE.md
`-- .gitignore
```

## UI Asset Update

The Air University logo is stored locally at `src/static/img/aulogo.png` and is loaded through Flask `url_for('static', ...)`, so the navbar no longer depends on an external image link.

## Main Features

- Admin registration
- Admin login/logout
- Secure password hashing
- Add student records
- View student records
- Edit student records
- Delete student records using POST requests
- Input validation using Flask-WTF
- CSRF protection on forms
- Environment-based secret configuration

## Security Improvements Applied

| Area | Improvement |
|---|---|
| Secrets | Removed `.env` and added `.env.example` |
| Passwords | Removed default `admin/admin`; passwords are hashed |
| CSRF | Removed CSRF exemptions and added CSRF tokens |
| Delete action | Changed delete from GET to POST |
| Sessions | Enabled HTTPOnly, SameSite, and environment-based Secure cookies |
| Production config | Blocks production startup if `SECRET_KEY` is left as the development fallback |
| Record lookups | Uses explicit 404 handling for missing student records |
| Repository hygiene | Removed `.git/`, virtual environment, database, and cache files |
| Code organization | Moved all application code into `src/` |

## How to Review

1. Read the report in `docs/`.
2. Review the source code in `src/`.
3. Check the screenshots in `screenshots/`.
4. Follow `RUN_GUIDE.md` to run the project locally.

## Academic Note

This is a coursework project for Secure Software Design and Development. It demonstrates secure coding principles in a small Flask CRUD web application.
