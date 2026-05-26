class Appointment:
    
    def __init__(self, appointment_id, name, date, time, reason): # Creates a new appointment object

        self.id = appointment_id
        self.name = name
        self.date = date
        self.time = time
        self.reason = reason

    def to_dict(self): # Convert object into dictionary

        return {
            "id": self.id,
            "name": self.name,
            "date": self.date,
            "time": self.time,
            "reason": self.reason
        }