import tkinter as tk
import re


def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."

    if not re.search(r'[A-Z]', password):
        return "Weak: Password must include at least one uppercase letter."

    if not re.search(r'[a-z]', password):
        return "Weak: Password must include at least one lowercase letter."

    if not re.search(r'\d', password):
        return "Weak: Password must include at least one number."

    if not re.search(r'[~!@#$%^&*(){}|:",.?]', password):
        return "Weak: Password must include at least one special character."

    return "Strong: Password meets all criteria."


def assess_password():
    password = password_entry.get()
    strength = check_password_strength(password)
    result_label.config(text=strength)


root = tk.Tk()
root.title("Password Strength Checker")

password_label = tk.Label(root, text="Enter Password:")
password_label.pack(pady=5)

password_entry = tk.Entry(root, width=50)
password_entry.pack(pady=5)

check_btn = tk.Button(root, text="Check Password", command=assess_password)
check_btn.pack(pady=5)

result_label = tk.Label(root, text="Password strength will be displayed here.")
result_label.pack(pady=20)

root.mainloop()
