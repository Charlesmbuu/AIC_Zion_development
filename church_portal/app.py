#TKN
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from models import db, User, Announcement, Sermon, Event, Blog, Notice, Donation, Suggestion
from config import Config
from datetime import datetime, timedelta
# For M-Pesa: pip install Flask-Mpesa
from flask_mpesa import MpesaAPI
import os

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# M-Pesa setup (placeholder - get keys from Safaricom)
mpesa = MpesaAPI(app, consumer_key='YOUR_CONSUMER_KEY', consumer_secret='YOUR_CONSUMER_SECRET',
                 shortcode='YOUR_SHORTCODE', passkey='YOUR_PASSKEY', callback_url='http://yourdomain/callback')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class FlaskUser(UserMixin):
    pass  # Extend if needed

# Create DB if not exists
with app.app_context():
    if not os.path.exists('instance/church.db'):
        db.create_all()
        # Create default admin
        admin = User(username='admin', password='adminpass', is_admin=True)
        db.session.add(admin)
        db.session.commit()

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:  # Hash in prod
            login_user(user)
            if user.is_admin:
                return redirect(url_for('admin_dashboard'))
            return redirect(url_for('member_dashboard'))
        flash('Invalid credentials')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if User.query.filter_by(username=username).first():
            flash('Username taken')
        else:
            user = User(username=username, password=password)
            db.session.add(user)
            db.session.commit()
            flash('Registered successfully')
            return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/member_dashboard')
@login_required
def member_dashboard():
    if current_user.is_admin:
        return redirect(url_for('admin_dashboard'))
    return render_template('member_dashboard.html')

@app.route('/admin_dashboard', methods=['GET', 'POST'])
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        return redirect(url_for('member_dashboard'))
    if request.method == 'POST':
        if 'announcement_title' in request.form:
            ann = Announcement(title=request.form['announcement_title'], content=request.form['announcement_content'])
            db.session.add(ann)
            db.session.commit()
            flash('Announcement posted')
        elif 'sermon_title' in request.form:
            ser = Sermon(title=request.form['sermon_title'], content=request.form['sermon_content'])
            db.session.add(ser)
            db.session.commit()
            flash('Sermon posted')
        elif 'event_title' in request.form:
            event = Event(
                title=request.form['event_title'],
                description=request.form['event_description'],
                date=datetime.strptime(request.form['event_date'], '%Y-%m-%dT%H:%M')
            )
            db.session.add(event)
            db.session.commit()
            flash('Event posted')
        elif 'blog_title' in request.form:
            blog = Blog(
                title=request.form['blog_title'],
                content=request.form['blog_content'],
                author=request.form['blog_author']
            )
            db.session.add(blog)
            db.session.commit()
            flash('Blog posted')
        elif 'notice_content' in request.form:
            notice = Notice(content=request.form['notice_content'])
            db.session.add(notice)
            db.session.commit()
            flash('Notice posted')
    suggestions = Suggestion.query.all()
    return render_template('admin_dashboard.html', suggestions=suggestions)

@app.route('/announcements')
@login_required
def announcements():
    four_months_ago = datetime.utcnow() - timedelta(days=120)
    fresh = Announcement.query.filter(Announcement.date_posted >= four_months_ago).order_by(Announcement.date_posted.desc()).all()
    old = Announcement.query.filter(Announcement.date_posted < four_months_ago).order_by(Announcement.date_posted.desc()).all()
    return render_template('announcements.html', fresh=fresh, old=old)

@app.route('/sermons')
@login_required
def sermons():
    four_months_ago = datetime.utcnow() - timedelta(days=120)
    fresh = Sermon.query.filter(Sermon.date >= four_months_ago).order_by(Sermon.date.desc()).all()
    old = Sermon.query.filter(Sermon.date < four_months_ago).order_by(Sermon.date.desc()).all()
    return render_template('sermons.html', fresh=fresh, old=old)

@app.route('/events')
@login_required
def events():
    # Show upcoming events only
    upcoming = Event.query.filter(Event.date >= datetime.utcnow()).order_by(Event.date).all()
    past = Event.query.filter(Event.date < datetime.utcnow()).order_by(Event.date.desc()).all()
    return render_template('events.html', upcoming=upcoming, past=past)

@app.route('/blogs')
@login_required
def blogs():
    four_months_ago = datetime.utcnow() - timedelta(days=120)
    fresh = Blog.query.filter(Blog.date_posted >= four_months_ago).order_by(Blog.date_posted.desc()).all()
    old = Blog.query.filter(Blog.date_posted < four_months_ago).order_by(Blog.date_posted.desc()).all()
    return render_template('blogs.html', fresh=fresh, old=old)

@app.route('/notices')
@login_required
def notices():
    four_months_ago = datetime.utcnow() - timedelta(days=120)
    fresh = Notice.query.filter(Notice.date_posted >= four_months_ago).order_by(Notice.date_posted.desc()).all()
    old = Notice.query.filter(Notice.date_posted < four_months_ago).order_by(Notice.date_posted.desc()).all()
    return render_template('notices.html', fresh=fresh, old=old)

@app.route('/donate', methods=['GET', 'POST'])
@login_required
def donate():
    if request.method == 'POST':
        amount = request.form['amount']
        phone = request.form['phone']  # Format: 2547xxxxxxxx
        response = mpesa.stk_push(phone, amount, 'Donation to Church')
        if response['ResponseCode'] == '0':
            # Save placeholder donation (real callback handles success)
            don = Donation(user_id=current_user.id, amount=amount, transaction_id=response['CheckoutRequestID'])
            db.session.add(don)
            db.session.commit()
            flash('Donation initiated')
        else:
            flash('Error initiating donation')
    return render_template('donate.html')

@app.route('/mpesa_callback', methods=['POST'])
def mpesa_callback():
    data = request.json
    # Handle success/failure, update Donation
    print(data)  # Log in prod
    return 'OK'

@app.route('/suggest', methods=['GET', 'POST'])
@login_required
def suggest():
    if request.method == 'POST':
        content = request.form['content']
        sug = Suggestion(user_id=current_user.id, content=content)
        db.session.add(sug)
        db.session.commit()
        flash('Suggestion submitted')
    return render_template('suggest.html')

if __name__ == '__main__':
    app.run(debug=True)
