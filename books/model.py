from flask_sqlalchemy import SQLAlchemy
from db import db


class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(191), nullable=True)
    image = db.Column(db.String(191), nullable=True)
    author_id = db.Column(db.Integer, db.ForeignKey("authors.id"), nullable=False)

    def __init__(self, name, description, image, author_id) -> None:
        self.name = name
        self.image = image
        self.description = description
        self.author_id = author_id

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "image": self.image,
            "author_id": self.author_id,
        }
