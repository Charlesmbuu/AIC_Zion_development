<!-- This is Kelvin -->
# Church Portal

A simple Python Flask-based church website portal for members and admins.

## Setup (Cross-Platform: Windows/Linux)
1. Install Python 3.12+ (from python.org or package manager).
2. Create virtualenv: `python -m venv venv`
3. Activate: Windows - `venv\Scripts\activate`; Linux - `source venv/bin/activate`
4. Install deps: `pip install flask flask-sqlalchemy flask-login flask-mpesa`
5. Run: `python app.py`
6. Access: http://127.0.0.1:5000
7. Default admin: username 'admin', password 'adminpass'

## Customization
- Add UI: Edit templates/static for engaging features (e.g., JS animations).
- M-Pesa: Replace placeholders with real keys. Test sandbox.

## Deployment
- Local: As above.
- Online: Upload to PythonAnywhere (free), create web app, point to app.py.
- Domain: Buy xyzchurch.com, set DNS to host.

## Features
- See proposal for details.

For production: Hash passwords, add HTTPS, backup DB.
