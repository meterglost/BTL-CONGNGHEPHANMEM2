from ..database import Database

class Session:
    model = Database.dbInstance['uwc']['session']

    @staticmethod
    def add(token) -> None:
        Session.model.insert_one({'token': token})

    @staticmethod
    def delete(token):
        pass

    @staticmethod
    def has(token) -> bool:
        return Session.model.find_one({'token': token}) is not None
