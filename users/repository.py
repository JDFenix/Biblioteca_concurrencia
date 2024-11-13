from users.model import db, User
from extensions import bcrypt


class UserRepository:

    @staticmethod
    def add_user(username, email, password):
        password_str = str(password)
        password_hash = bcrypt.generate_password_hash(
            password_str.encode("utf-8")
        ).decode("utf-8")
        new_user = User(username=username, email=email, password=password_hash)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def update_user(user_id, username=None, email=None, password=None):
        user = User.query.get(user_id)
        if user:
            if username:
                user.username = username
            if email:
                user.email = email
            if password:
                user.password = password
            db.session.commit()
        return user

    @staticmethod
    def delete_user(user_id):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
        return user
