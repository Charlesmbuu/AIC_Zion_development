# Church Portal

A lightweight, Python Flask-based church website portal designed to foster spiritual growth and community engagement through member and admin interfaces. Built for cross-platform development on Windows and Linux, it supports local testing and scalable online deployment.

## Features

### Member Portal:
- Sign-up/login to access content, symbolizing faith commitment.
- View fresh (within 4 months) and archived announcements, sermons, events, blogs, and notices.
- Donate via M-Pesa Daraja API for church projects, harambees, or self-help groups.
- Submit suggestions/feedback via a digital suggestion box.
- Inspirational features: Prayer requests, Bible verse of the day (customizable).

### Admin Portal:
- Post/manage announcements, sermons, events, blogs, and notices.
- View/respond to suggestions and donation logs for transparency.
- User management for member approvals.

### Additional Highlights:
- **Customizable UI/UX:** Bootstrap-based, ready for engaging additions (e.g., animations, themes).
- **Transparency:** Donation and suggestion records stored securely.
- **Lightweight:** Minimal RAM/ROM usage (~100MB locally).

## Prerequisites

- Python 3.12+ (download from [https://www.python.org](https://www.python.org))
- Git (optional for version control)
- Internet browser

## Setup (Windows/Linux)

1. Clone or download the project to your local machine.
2. Create a virtual environment:
   ```bash
   # Windows
   python -m venv venv
   # Linux
   python3 -m venv venv
   ```
3. Activate the virtual environment:
   ```bash
   # Windows
   venv\Scripts\activate
   # Linux
   source venv/bin/activate
   ```
4. Install dependencies:
   ```bash
   pip install flask flask-sqlalchemy flask-login flask-mpesa
   ```
5. Run the app:
   ```bash
   python app.py
   ```
6. Access the app at [http://127.0.0.1:5000](http://127.0.0.1:5000)

**Default admin:** username `admin`, password `adminpass`.

## Project Structure

```
church_portal/
├── app.py              # Main application
├── models.py           # Database models
├── config.py           # Configuration
├── templates/          # HTML templates
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   ├── member_dashboard.html
│   ├── admin_dashboard.html
│   ├── announcements.html
│   ├── sermons.html
│   ├── events.html
│   ├── blogs.html
│   ├── notices.html
│   ├── donate.html
│   ├── suggest.html
├── static/             # CSS/JS files
│   ├── css/
│   │   └── style.css
├── instance/           # SQLite DB
│   └── church.db
└── README.md
```

## Online Deployment

### Free Hosting:
- **PythonAnywhere:** Free tier, easy Flask setup. Upload files via dashboard, configure WSGI.
- **Render:** Free hobby tier, auto-deploys from Git.
- **Fly.io:** Free tier with 3 machines.

### Paid Hosting (budget-dependent):
- Hostinger (~$3/month)
- DigitalOcean ($5/month)
- AWS Lightsail ($3.50/month)

**Domain:** Purchase via Namecheap/GoDaddy (~$10/year, e.g., xyzchurch.com). Point DNS to host.  
**M-Pesa Callback:** Set callback URL to host's external URL (e.g., `yourdomain.com/mpesa_callback`).

## M-Pesa Integration

1. Obtain API keys from Safaricom Daraja portal (free sandbox).
2. Update `app.py` with consumer key, secret, shortcode, and passkey.
3. Test STK Push in sandbox mode before production.

## Customization

- **UI/UX:** Edit `templates/` and `static/css/style.css` for engaging features (e.g., animations, dark mode).
- **Features:** Add prayer requests, forums, or email notifications (e.g., via Flask-Mail).
- **Security:** For production, use bcrypt for password hashing, enable HTTPS, and backup `church.db`.

## Production Notes

- Replace plaintext passwords with hashed passwords.
- Configure HTTPS for secure online access.
- Regularly back up the SQLite database (`instance/church.db`).
- Monitor hosting limits; upgrade as traffic grows.

## Testing

- Local: Run on Windows 11/Linux (e.g., Parrot Security Edition) with `python app.py`.
- Test member/admin flows: Register, login, post content, donate, submit suggestions.
- Verify cross-OS compatibility (uses virtualenv for consistency).

## Troubleshooting

- **Database Issues:** Delete `instance/church.db` and rerun `app.py` to recreate.
- **M-Pesa Errors:** Check API keys and sandbox status.
- **Hosting:** Ensure WSGI settings match `app.py`.

## Future Enhancements

- Live suggestion responses (e.g., via WebSocket).
- Mobile app integration.
- Advanced analytics for donation tracking.

---

For issues or contributions, contact the developer or fork the repository.
