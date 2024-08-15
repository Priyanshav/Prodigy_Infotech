import tkinter as tk
from tkinter import messagebox


def caesar_cipher(text, shift):
    result = []
    shift = shift % 26

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result.append(chr(start+(ord(char) - start + shift) % 26))
        else:
            result.append(char)
    return ''.join(result)


def encrypt():
    msg = msg_entry.get()
    try:
        shift = int(shift_entry.get())
        encrypted_msg = caesar_cipher(msg, shift)
        result_label.config(text=f"Encrypted Message: {encrypted_msg}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be an integer.")


def decrypt():
    msg = msg_entry.get()
    try:
        shift = int(shift_entry.get())
        decrypted_msg = caesar_cipher(msg, 0)
        result_label.config(text=f"Decrypted Message: {decrypted_msg}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be an integer.")


root = tk.Tk()
root.title("Caesar Cipher")

msg_label = tk.Label(root, text="Enter Message:")
msg_label.pack(pady=5)

msg_entry = tk.Entry(root, width=50)
msg_entry.pack(pady=5)

shift_label = tk.Label(root, text="Enter Shift Value:")
shift_label.pack(pady=5)

shift_entry = tk.Entry(root, width=10)
shift_entry.pack(pady=5)

encrypt_btn = tk.Button(root, text="Encrypt", command=encrypt)
encrypt_btn.pack(pady=5)

decrypt_btn = tk.Button(root, text="Decrypt", command=decrypt)
decrypt_btn.pack(pady=5)

result_label = tk.Label(root, text="Result will be displayed here.")
result_label.pack(pady=20)

root.mainloop()
