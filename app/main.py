from appointment_manager import (
    add_appointment,
    view_appointments,
    delete_appointment,
    update_appointment
)


while True:

    print("\n===== Appointment System =====")

    print("1. Add Appointment")
    print("2. View Appointments")
    print("3. Delete Appointment")
    print("4. Update Appointment")
    print("5. Exit")

    choice = input("Choose an option: ")

    # Add appointment
    if choice == "1":

        name = input("Enter name: ")
        date = input("Enter date (DD-MM-YYYY): ")
        time = input("Enter time (HH:MM): ")
        reason = input("Enter reason: ")

        add_appointment(
            name,
            date,
            time,
            reason
        )

    # View appointments
    elif choice == "2":

        view_appointments()

    # Delete appointment
    elif choice == "3":

        appointment_id = int(
            input("Enter appointment ID to delete: ")
        )

        delete_appointment(appointment_id)

    # Update appointment
    elif choice == "4":

        appointment_id = int(
            input("Enter appointment ID to update: ")
        )

        new_name = input("Enter new name: ")
        new_date = input("Enter new date (DD-MM-YYYY): ")
        new_time = input("Enter new time: ")
        new_reason = input("Enter new reason: ")

        update_appointment(
            appointment_id,
            new_name,
            new_date,
            new_time,
            new_reason
        )

    # Exit system
    elif choice == "5":

        print("Program closed.")
        break

    else:
        print("Invalid option.")