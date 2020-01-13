from datetime import datetime
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask import request
import os

app = Flask(__name__)
Bootstrap(app)

#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = 'sqlite:///{}'.format(os.path.join(project_dir, 'db.sqlite3'))

app.config['SQLALCHEMY_DATABASE_URI'] = database_file

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))

    def __repr__(self):
        return '<Username: {}>'.format(self.username)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():

    return render_template('login.html')


@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.form:
        name = request.form['username']

        #username = User(username=request.form.get('username'))
        #email = User(email=request.form.get('email'))
        #password = User(password=request.form.get('password'))

        signature = User(username=name)
        db.session.add(signature)
        #db.session.add_all([username, email, password])
        db.session.commit()
        print(request.form)

    users = User.query.all()
    return render_template('signup.html', username=users)


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


if __name__ == '__main__':
    app.run(debug=True)
