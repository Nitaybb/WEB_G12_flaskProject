from utilities.db.db_manager import dbManager

class users:
    def __init__(self, ID=None, first_name=None, last_name=None,
                 phone_number=None, email=None, gender=None):
        self.ID = ID
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.gender = gender
