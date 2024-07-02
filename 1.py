import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('hospital.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table for patients
cursor.execute('''CREATE TABLE IF NOT EXISTS patients (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    gender TEXT NOT NULL,
                    diagnosis TEXT NOT NULL)''')

# Function to add a new patient
def add_patient(name, age, gender, diagnosis):
    cursor.execute("INSERT INTO patients (name, age, gender, diagnosis) VALUES (?, ?, ?, ?)", 
                   (name, age, gender, diagnosis))
    conn.commit()
    print("Patient added successfully!")

# Function to view all patients
def view_patients():
    cursor.execute("SELECT * FROM patients")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Function to delete a patient by ID
def delete_patient(patient_id):
    cursor.execute("DELETE FROM patients WHERE id=?", (patient_id,))
    conn.commit()
    print("Patient deleted successfully!")

# Main menu
def main_menu():
    while True:
        print("\nHospital DBMS")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Delete Patient")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter patient name: ")
            age = int(input("Enter patient age: "))
            gender = input("Enter patient gender: ")
            diagnosis = input("Enter diagnosis: ")
            add_patient(name, age, gender, diagnosis)
        elif choice == '2':
            view_patients()
        elif choice == '3':
            patient_id = int(input("Enter patient ID to delete: "))
            delete_patient(patient_id)
        elif choice == '4':
            break
        else:
            print("Invalid choice! Please try again.")

# Run the main menu
if __name__ == "__main__":
    main_menu()

# Close the connection
conn.close()
