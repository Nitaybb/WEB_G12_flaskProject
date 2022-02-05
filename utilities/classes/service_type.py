from utilities.db.db_manager import dbManager

class service_type:
    def __init__(self, service_ID=None, name=None, duration=None):
        self.service_ID = service_ID
        self.name = name
        self.duration = duration

