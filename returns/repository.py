from returns.model import Return
from db import db


class ReturnRepository:

    @staticmethod
    def get_all_returns():
        return Return.query.all()

    @staticmethod
    def get_return_by_id(return_id):
        return Return.query.get(return_id)

    @staticmethod
    def add_return(lending_id, return_date, condition):
        new_return = Return(
            lending_id=lending_id, return_date=return_date, condition=condition
        )
        db.session.add(new_return)
        db.session.commit()
        return new_return

    @staticmethod
    def update_return(return_id, lending_id=None, return_date=None, condition=None):
        return_record = Return.query.get(return_id)
        if return_record:
            if lending_id:
                return_record.lending_id = lending_id
            if return_date:
                return_record.return_date = return_date
            if condition:
                return_record.condition = condition
            db.session.commit()
        return return_record

    @staticmethod
    def delete_return(return_id):
        return_record = Return.query.get(return_id)
        if return_record:
            db.session.delete(return_record)
            db.session.commit()
        return return_record
