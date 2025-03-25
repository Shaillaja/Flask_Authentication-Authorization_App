from flask import Flask, render_template, request, redirect, session, flash
from functools import wraps
from database.db import db, User, create_tables
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "your_secret_key"

# PostgreSQL Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:***@127.0.0.1:5432/flask_app"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

with app.app_context():
    create_tables()

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user" not in session:
            flash("You need to log in first!", "warning")
            return redirect("/")
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def home():
    if "user" in session:
        return f"Welcome, {session['user']}! <br><a href='/logout'>Logout</a>"
    return render_template("login.html")

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template("result.html",username=session['user'])

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("Username already exists!", "danger")
            return redirect('/register')
        
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash("Registration successful! You can log in now.", "success")
        return redirect('/')
    return render_template("register.html")

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = User.query.filter_by(username=username).first()
    print(user, password)
    if user and check_password_hash(user.password, password):
        session['user'] = username
        return redirect('/dashboard')
    else:
        flash("Invalid username or password!", "danger")
        return render_template("login.html", show_alert=True)

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash("You have been logged out.", "info")
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
