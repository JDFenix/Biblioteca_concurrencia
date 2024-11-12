from flask import Flask
from users.route import users_bp
from books.route import books_bp
from users.model import db
from db import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/biblioteca"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


app.register_blueprint(users_bp, url_prefix="/api")
app.register_blueprint(books_bp, url_prefix="/api")


if __name__ == "__main__":
    app.run(debug=True)
