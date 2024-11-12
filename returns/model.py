from db import db


class Return(db.Model):
    __tablename__ = "returns"

    id = db.Column(db.Integer, primary_key=True)
    lending_id = db.Column(db.Integer, db.ForeignKey("lendings.id"), nullable=False)
    return_date = db.Column(db.Date, nullable=False)
    condition = db.Column(
        db.String(50), nullable=False
    )  # Condición del libro al devolverlo

    def to_dict(self):
        return {
            "id": self.id,
            "lending_id": self.lending_id,
            "return_date": self.return_date.isoformat(),
            "condition": self.condition,
        }
