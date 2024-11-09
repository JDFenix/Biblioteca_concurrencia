from users.repository import UserRepository
from users.model import User


class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def get_user(self, user_id: int) -> User:
        return self.user_repo.get_user_by_id(user_id)

    def create_user(self, username: str, email: str) -> User:
        return self.user_repo.add_user(username, email)

    def update_user(
        self, user_id: int, username: str = None, email: str = None
    ) -> User:
        return self.user_repo.update_user(user_id, username, email)

    def delete_user(self, user_id: int) -> User:
        return self.user_repo.delete_user(user_id)

    def get_all_users(self) -> list:
        return self.user_repo.get_all_users()
