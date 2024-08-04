import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("500x200")

        self.length_label = tk.Label(root, text="Length:")
        self.length_label.grid(row=0, column=0)

        self.length_entry = tk.Entry(root, width=10)
        self.length_entry.grid(row=0, column=1)

        self.length_tip = tk.Label(root, text="(min 6, max 128)", fg="gray")
        self.length_tip.grid(row=0, column=2)

        self.include_uppercase = tk.BooleanVar()
        self.include_uppercase.set(True)
        self.uppercase_checkbox = tk.Checkbutton(root, text="Uppercase", variable=self.include_uppercase)
        self.uppercase_checkbox.grid(row=1, column=0)

        self.include_numbers = tk.BooleanVar()
        self.include_numbers.set(True)
        self.numbers_checkbox = tk.Checkbutton(root, text="Numbers", variable=self.include_numbers)
        self.numbers_checkbox.grid(row=1, column=1)

        self.include_special_chars = tk.BooleanVar()
        self.include_special_chars.set(True)
        self.special_chars_checkbox = tk.Checkbutton(root, text="Special Chars", variable=self.include_special_chars)
        self.special_chars_checkbox.grid(row=2, column=0)

        self.generate_button = tk.Button(root, text="Generate", command=self.generate_password)
        self.generate_button.grid(row=3, column=0, columnspan=2)

        self.password_label = tk.Label(root, text="Password:")
        self.password_label.grid(row=4, column=0)

        self.password_entry = tk.Entry(root, width=40)
        self.password_entry.grid(row=4, column=1)

        self.copy_button = tk.Button(root, text="Copy", command=self.copy_password)
        self.copy_button.grid(row=4, column=2)

        self.strength_label = tk.Label(root, text="Strength:")
        self.strength_label.grid(row=5, column=0)

        self.strength_meter = tk.Label(root, text="", fg="gray")
        self.strength_meter.grid(row=5, column=1)

    def generate_password(self):
        length = int(self.length_entry.get())
        if length < 6 or length > 128:
            messagebox.showerror("Error", "Length must be between 8 and 128")
            return
        chars = string.ascii_lowercase
        if self.include_uppercase.get():
            chars += string.ascii_uppercase
        if self.include_numbers.get():
            chars += string.digits
        if self.include_special_chars.get():
            chars += string.punctuation
        password = ''.join(random.choice(chars) for _ in range(length))
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)
        self.update_strength_meter(password)

    def copy_password(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.password_entry.get())
        messagebox.showinfo("Copied", "Password copied to clipboard")

    def update_strength_meter(self, password):
        strength = self.calculate_password_strength(password)
        if strength < 20:
            self.strength_meter.config(text="Weak", fg="red")
        elif strength < 40:
            self.strength_meter.config(text="Medium", fg="orange")
        else:
            self.strength_meter.config(text="Strong", fg="green")

    def calculate_password_strength(self, password):
        strength = 0
        if len(password) >= 12:
            strength += 20
        if any(c.isupper() for c in password):
            strength += 10
        if any(c.isdigit() for c in password):
            strength += 10
        if any(c in string.punctuation for c in password):
            strength += 10
        return strength

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    password_generator = PasswordGenerator(root)
    password_generator.run()