# Project Notes

## Project Name

Secure Student Management System

## Purpose

The purpose of this project is to demonstrate secure software design and development practices using a Flask-based Student Management System.

## What Was Cleaned

The original ZIP contained files that should not be committed to GitHub. The final repository removes:

```text
.env
.git/
env/
__pycache__/
instance/firstapp.db
*.pyc
```

## Main Security Fixes

- CSRF exemptions were removed.
- Login and registration now use Flask-WTF forms.
- Delete operation now uses POST instead of GET.
- Default admin/admin creation was removed.
- Admin creation from environment variables is optional.
- Production startup now requires a configured `SECRET_KEY`.
- Login, logout, and first-admin registration clear stale session data.
- Missing student records now return explicit 404 responses through the current SQLAlchemy session API.
- Runtime database is excluded from GitHub.
- All application code is placed inside `src/`.

## Technical Review - 2026-07-07

- Reviewed Flask app factory, models, forms, templates, Dockerfile, and run guide.
- Confirmed CSRF coverage on registration, login, dashboard create, update, delete, logout, and dashboard redirect forms.
- Hardened session handling to reduce stale-session and session-fixation risk.
- Added a production guard so the app cannot run with the development fallback secret.
- Replaced legacy record lookup helpers with explicit `db.session.get(...)` and 404 handling.

## Application Code

All code is stored in:

```text
src/
```

This includes:

```text
src/app.py
src/forms.py
src/create_db.py
src/templates/
src/static/
```

## Limitations

- SQLite is used for academic simplicity.
- Only a single admin workflow is implemented.
- No role-based access control is included.
- No login rate limiting is included yet.
- Inline CSS is still used in templates.

## Future Improvements

- Add role-based access control.
- Add login rate limiting.
- Add password confirmation and complexity rules.
- Add audit logs for CRUD operations.
- Add unit tests.
- Move inline CSS into static CSS files.


## UI Asset Update

The navbar logo was changed from an external URL to a local static asset stored at `src/static/img/aulogo.png`. This makes the app work offline and avoids broken logo links.
