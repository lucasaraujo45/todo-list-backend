from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String(80), unique=False, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    address = db.Column(db.String(120), unique=False, nullable=True)
    phone = db.Column(db.String(120), unique=True, nullable=True)

    def __repr__(self):
        'Person(todo='+self.todo+', email='+self.email+ ')'
    def serialize(self):
        return {
            "todo": self.todo,
            "email": self.email,
            "address": self.address,
            "phone": self.phone
        }
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String(80), unique=False, nullable=True)
    completed = db.Column(db.Boolean, unique=True, nullable=False)

    def __repr__(self):
        'Contact(todo='+self.todo+', email='+self.email+ ')'
    def serialize(self):
        return {
            "username": self.username,
            "email": self.email,
            "address": self.address,
            "phone": self.phone
        }