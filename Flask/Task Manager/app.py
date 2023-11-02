from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo
from flask_login import UserMixin, login_user, logout_user, login_required
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_manager.db'
db = SQLAlchemy(app)

@app.route('/')
def index():
        return("Hello World")

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(max=80)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(max=80)])
    password = PasswordField('Password', validators=[DataRequired()])

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User(username = username, password = password)
        db.session.add(user)
        db.session.commit()
        flash("you did it")
        return redirect('login')
    return render_template('register.html', form = form)

    
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # user can contain nonw also when we didn't find that user in database
        user = User.query.filter_by(username=form.username.data)
        if user and user.password == form.password.data:
            login_user(user)
            flash("Login successful.")
            return redirect(url_for('index'))
        else:
            flash("Login failed. Please check your username and password")

    return render_template('login.html',form=form)
    
@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out")
    return redirect("index")

    
if __name__ == '__main__':
    app.run(debug=True)