from returns.repository import ReturnRepository


class ReturnService:

    def __init__(self, return_repository: ReturnRepository) -> None:
        self.return_repository = return_repository

    def get_all_returns(self):
        return self.return_repository.get_all_returns()

    def get_return_by_id(self, return_id):
        return self.return_repository.get_return_by_id(return_id)

    def add_return(self, lending_id, return_date, condition):
        return self.return_repository.add_return(lending_id, return_date, condition)

    def update_return(
        self, return_id, lending_id=None, return_date=None, condition=None
    ):
        return self.return_repository.update_return(
            return_id, lending_id, return_date, condition
        )

    def delete_return(self, return_id):
        return self.return_repository.delete_return(return_id)
