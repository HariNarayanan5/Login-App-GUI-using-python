import tkinter as tk
import time

# Simulated user database
user_database = {
    "user": "password",
    "john": "123456",
    # Add more users if needed
}

def validate_login(username, password):
    # Simulated login validation
    return username in user_database and user_database[username] == password

def login_animation():
    def animate():
        username = username_entry.get()
        password = password_entry.get()

        # Simulate login validation
        if validate_login(username, password):
            login_status.set("Login successful!")
        else:
            login_status.set("Invalid credentials. Please try again.")

    def register():
        new_username = new_username_entry.get()
        new_password = new_password_entry.get()

        # Simulate user registration
        if new_username and new_password:
            user_database[new_username] = new_password
            register_status.set("Registration successful!")
        else:
            register_status.set("Invalid input. Please try again.")

    root = tk.Tk()
    root.title("Login System")

    login_frame = tk.Frame(root)
    login_frame.pack(padx=20, pady=10)

    # Login Section
    login_lbl = tk.Label(login_frame, text="Login", font=("Arial", 16))
    login_lbl.grid(row=0, column=0, columnspan=2, pady=5)

    username_label = tk.Label(login_frame, text="Username:")
    username_label.grid(row=1, column=0)
    username_entry = tk.Entry(login_frame)
    username_entry.grid(row=1, column=1)

    password_label = tk.Label(login_frame, text="Password:")
    password_label.grid(row=2, column=0)
    password_entry = tk.Entry(login_frame, show="*")
    password_entry.grid(row=2, column=1)

    login_btn = tk.Button(login_frame, text="Login", command=animate)
    login_btn.grid(row=3, column=0, columnspan=2, pady=10)

    login_status = tk.StringVar()
    login_status.set("Login status will appear here.")
    login_status_lbl = tk.Label(login_frame, textvariable=login_status, fg="blue")
    login_status_lbl.grid(row=4, column=0, columnspan=2)

    # Registration Section
    register_frame = tk.Frame(root)
    register_frame.pack(padx=20, pady=10)

    register_lbl = tk.Label(register_frame, text="Register", font=("Arial", 16))
    register_lbl.grid(row=0, column=0, columnspan=2, pady=5)

    new_username_label = tk.Label(register_frame, text="New Username:")
    new_username_label.grid(row=1, column=0)
    new_username_entry = tk.Entry(register_frame)
    new_username_entry.grid(row=1, column=1)

    new_password_label = tk.Label(register_frame, text="New Password:")
    new_password_label.grid(row=2, column=0)
    new_password_entry = tk.Entry(register_frame, show="*")
    new_password_entry.grid(row=2, column=1)

    register_btn = tk.Button(register_frame, text="Register", command=register)
    register_btn.grid(row=3, column=0, columnspan=2, pady=10)

    register_status = tk.StringVar()
    register_status.set("Registration status will appear here.")
    register_status_lbl = tk.Label(register_frame, textvariable=register_status, fg="green")
    register_status_lbl.grid(row=4, column=0, columnspan=2)

    root.mainloop()

login_animation()
