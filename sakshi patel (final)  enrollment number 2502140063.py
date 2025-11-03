"""      NAME - SAKSHI PATEL       ENROLLMENT NUMBER - 2502140063       """


from datetime import datetime

# Password for login
PASSWORD = ("pass123")

# Data storage (in memory only)
appointments = []
patients = []
available_slots = []

# Create some available time slots for today
def setup_slots():
    today = str(datetime.today().date())
    for t in ["09:00", "10:00", "11:00", "14:00", "15:00"]:
        available_slots.append((today, t))

# Function to add new patient
def add_patient():
    name = input("Enter patient name: ")
    contact = input("Enter contact number: ")
    patient_id = len(patients) + 1
    patient = {"id": patient_id, "name": name, "contact": contact}
    patients.append(patient)
    print(f"Patient added successfully! ID: {patient_id}")

# Function to show all patients
def view_patients():
    if not patients:
        print("No patients found.")
    else:
        for p in patients:
            print(f"ID: {p['id']}, Name: {p['name']}, Contact: {p['contact']}")

# Function to book appointment
def schedule_appointment():
    if not patients:
        print("No patients found. Please add a patient first.")
        return
    patient_id = int(input("Enter patient ID: "))
    found = False
    for p in patients:
        if p['id'] == patient_id:
            found = True
            break
    if not found:
        print("Invalid patient ID.")
        return

    doctor = input("Enter doctor name: ")
    date = input("Enter date (YYYY-MM-DD): ")
    time = input("Enter time (HH:MM): ")

    slot = (date, time)
    if slot not in available_slots:
        print("Sorry, this slot is not available.")
        return

    appointment_id = len(appointments) + 1
    appointment = {
        "id": appointment_id,
        "patient_id": patient_id,
        "doctor": doctor,
        "date": date,
        "time": time
    }
    appointments.append(appointment)
    available_slots.remove(slot)
    print("Appointment booked successfully!")

# Function to show all appointments
def view_appointments():
    if not appointments:
        print("No appointments found.")
    else:
        for a in appointments:
            print(f"ID: {a['id']}, Patient ID: {a['patient_id']}, Doctor: {a['doctor']}, Date: {a['date']}, Time: {a['time']}")

# Function to delete appointment
def delete_appointment():
    appt_id = int(input("Enter appointment ID to delete: "))
    for a in appointments:
        if a['id'] == appt_id:
            available_slots.append((a['date'], a['time']))
            appointments.remove(a)
            print("Appointment deleted successfully!")
            return
    print("Appointment not found.")

# Function to count total appointments
def total_appointments():
    print(f"Total Appointments: {len(appointments)}")

# Login function
def login():
    pwd = input("Enter password: ")
    if pwd == PASSWORD:
        return True
    else:
        print("Wrong password!")
        return False

# Menu function
def menu():
    print("--- Clinic Appointment Scheduler ---")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Schedule Appointment")
    print("4. View Appointments")
    print("5. Delete Appointment")
    print("6. Show Total Appointments")
    print("7. Exit")

# Main program
def main():
    setup_slots()
    if not login():
        return

    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_patient()
        elif choice == "2":
            view_patients()
        elif choice == "3":
            print("Available slots:", available_slots)
            schedule_appointment()
        elif choice == "4":
            view_appointments()
        elif choice == "5":
            delete_appointment()
        elif choice == "6":
            total_appointments()
        elif choice == "7":
            print("Thank you for using Clinic Scheduler!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
