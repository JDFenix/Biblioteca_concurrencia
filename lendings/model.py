# lendings/model.py
from db import db


class Lending(db.Model):
    __tablename__ = "lendings"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"), nullable=False)
    return_id = db.Column(db.Integer, db.ForeignKey("returns.id"), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "book_id": self.book_id,
            "return_id": self.return_id,
        }
