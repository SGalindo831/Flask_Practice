from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # Auto increments
    username = db.Column(db.String(80), unique=True, nullable=False) # Username must be unique
    email = db.Column(db.String(120), unique=True, nullable=False) # Email must be unique
    password_hash = db.Column(db.String(200), nullable=False) # The password will be hashed for security

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f'<User {self.username}>'