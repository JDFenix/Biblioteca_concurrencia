from flask import Flask, redirect, url_for
from users.route import users_bp
from books.route import books_bp
from books.route import books_views_bp
from lendings.route import lendings_bp
from authors.route import authors_bp
from returns.route import returns_bp
from users.model import db, User
from flask_login import LoginManager
from extensions import bcrypt
from auth.route import auth_bp
from db import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/biblioteca"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "supersecretkey"

db.init_app(app)
bcrypt.init_app(app)

login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = "auth.login"


app.register_blueprint(users_bp, url_prefix="/api")

app.register_blueprint(books_bp, url_prefix="/api")
app.register_blueprint(books_views_bp, url_prefix="/books")

app.register_blueprint(lendings_bp, url_prefix="/api")
app.register_blueprint(authors_bp, url_prefix="/api")
app.register_blueprint(returns_bp, url_prefix="/api")

app.register_blueprint(auth_bp, url_prefix="/auth")


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/")
def home():
    return redirect(url_for("books_views.home"))


if __name__ == "__main__":
    app.run(debug=True)
