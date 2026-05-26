from models import Appointment
from storage import load_appointments, save_appointments


def add_appointment(name, date, time, reason): # Add new appointment

    appointments = load_appointments()

    appointment_id = len(appointments) + 1

    new_appointment = Appointment(
        appointment_id,
        name,
        date,
        time,
        reason
    )

    appointments.append(
        new_appointment.to_dict()
    )

    save_appointments(appointments)

    print("Appointment added successfully!")


def view_appointments(): # Show all appointments

    appointments = load_appointments()

    if not appointments:
        print("No appointments found.")
        return

    for appointment in appointments:

        print("\n----------------------")

        print(f"ID: {appointment['id']}")
        print(f"Name: {appointment['name']}")
        print(f"Date: {appointment['date']}")
        print(f"Time: {appointment['time']}")
        print(f"Reason: {appointment['reason']}")


def delete_appointment(appointment_id): # Delete appointment by ID

    appointments = load_appointments()

    updated_appointments = []

    for appointment in appointments:

        if appointment["id"] != appointment_id:
            updated_appointments.append(appointment)

    save_appointments(updated_appointments)

    print("Appointment deleted successfully!")


# Update appointment
def update_appointment(
    appointment_id,
    new_name,
    new_date,
    new_time,
    new_reason
):

    appointments = load_appointments()

    for appointment in appointments:

        if appointment["id"] == appointment_id:

            appointment["name"] = new_name
            appointment["date"] = new_date
            appointment["time"] = new_time
            appointment["reason"] = new_reason

    save_appointments(appointments)

    print("Appointment updated successfully!")