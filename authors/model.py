from db import db


class Author(db.Model):
    __tablename__ = "authors"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    birth_year = db.Column(db.Integer, nullable=True)

    def __init__(self, first_name, last_name, birth_year) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_year": self.birth_year,
        }
