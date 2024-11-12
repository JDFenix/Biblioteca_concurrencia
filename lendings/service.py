from lendings.repository import LendingRepository


class LendingService:

    def __init__(self, lending_repository: LendingRepository) -> None:
        self.lending_repository = lending_repository

    def get_all_lendings(self):
        return self.lending_repository.get_all_lendings()

    def get_lending_by_id(self, lending_id):
        return self.lending_repository.get_lending_by_id(lending_id)

    def add_lending(self, user_id, book_id, return_id):
        return self.lending_repository.add_lending(user_id, book_id, return_id)

    def update_lending(self, lending_id, user_id=None, book_id=None, return_id=None):
        return self.lending_repository.update_lending(
            lending_id, user_id, book_id, return_id
        )

    def delete_lending(self, lending_id):
        return self.lending_repository.delete_lending(lending_id)
