from utilities.db.db_manager import dbManager

class users:
    def __init__(self, Appointment_ID=None, service_type=None,
                 scheduled_date=None, scheduled_time=None):
        self.Appointment_ID = Appointment_ID
        self.service_type = service_type
        self.scheduled_date = scheduled_date
        self.scheduled_time = scheduled_time
