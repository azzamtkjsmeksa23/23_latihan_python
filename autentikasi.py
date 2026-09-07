import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Azzam@123",  # password mu
        database="azzam_database" #database mu
    )

def setup_table():
    try:
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL
        )
        """)
        db.commit()
        cursor.close()
        db.close()
    except mysql.connector.Error as err:
        print(f"Gagal setup tabel: {err}")

def register():
    print("\n--- REGISTRATION ---")
    username = str(input("Enter a new username: ")).strip()
    password = str(input("Enter a new password: ")).strip()
    
    if not username or not password:
        print("Username dan password tidak boleh kosong.")
        return
    
    try:
        db = get_db_connection()
        cursor = db.cursor()
        # Password langsung dimasukkan sebagai teks biasa
        sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
        cursor.execute(sql, (username, password))
        db.commit()
        print("Registration successful! You can now log in.")
    except mysql.connector.Error as err:
        if err.errno == 1062:  # Username kembar
            print("Error: Username tersebut sudah terpakai.")
        else:
            print(f"An error occurred: {err}")
    finally:
        if 'db' in locals() and db.is_connected():
            cursor.close()
            db.close()

def login():
    print("\n--- LOGIN ---")
    username = str(input("Username: ")).strip()
    password = str(input("Password: ")).strip()
    
    try:
        db = get_db_connection()
        cursor = db.cursor()
        # Mencocokkan teks password secara langsung
        sql = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(sql, (username, password))
        user = cursor.fetchone()
        
        if user:
            print(f"\nWelcome back, {username}! Login successful.")
            return True
        else:
            print("\nInvalid username or password.")
            return False
    except mysql.connector.Error as err:
        print(f"Koneksi bermasalah saat login: {err}")
        return False
    finally:
        if 'db' in locals() and db.is_connected():
            cursor.close()
            db.close()

def main_menu():
    setup_table()
    while True:
        print("\n===== MAIN MENU =====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option (1-3): ").strip()
        
        if choice == "1":
            register()
        elif choice == "2":
            if login():
                break 
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main_menu()
