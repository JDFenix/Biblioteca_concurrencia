from flask import Flask, request, redirect, url_for, render_template, flash, Blueprint
from flask_login import login_user, logout_user, login_required
from users.model import User
from extensions import bcrypt


auth_bp = Blueprint("auth", __name__, template_folder="templates")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for("books_views.home"))
        else:
            return render_template("login.html", error="Invalid username or password")

    return render_template("login.html")


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
