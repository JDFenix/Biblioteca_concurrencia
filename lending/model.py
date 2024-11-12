from flask_sqlalchemy import SQLAlchemy
from db import db


class Lending(db.Model):
    __tablename__ = "lending"

    id = db.Column(db.Integer, primary_key=True)
    id_users = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    id_libro = db.Column(db.String(191), nullable=True)
    date_lending = db.Column(db.String(191), nullable=True)
    date_return = db.Column(db.Date, nullable=True)

    def __init__(self, id_users, id_libro, date_lending, date_return) -> None:
        self.id_users = id_users
        self.date_lending = date_lending
        self.id_libro = id_libro
        self.date_return = date_return

    def to_dict(self):
        return {
            "id": self.id,
            "id_users": self.id_users,
            "id_libro": self.id_libro,
            "date_lending": self.date_lending,
            "date_return": self.date_return,
        }
