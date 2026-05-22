import tkinter as tk
from tkinter import messagebox

students = []

def add_student():
    name = entry_name.get()
    student_id = entry_id.get()
    email = entry_email.get()
    phone = entry_phone.get()
    course = entry_course.get()
    year = entry_year.get()

    if name == "" or student_id == "" or email == "" or phone == "" or course == "" or year == "":
        messagebox.showerror("Error", "Please fill in all fields")
        return

    student = f"{name} | {student_id} | {email} | {phone} | {course} | {year}"
    students.append(student)

    text_area.insert(tk.END, student + "\n")
    clear_fields()

def clear_fields():
    entry_name.delete(0, tk.END)
    entry_id.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_course.delete(0, tk.END)
    entry_year.delete(0, tk.END)

# Window
root = tk.Tk()
root.title("Student Management System")
root.geometry("700x550")
root.configure(bg="#ffd6e8")   # pink background

# Title
title = tk.Label(
    root,
    text="Student Management System",
    font=("Comic Sans MS", 20, "bold"),
    fg="#d63384",
    bg="#ffd6e8"
)
title.grid(row=0, column=0, columnspan=2, pady=15)

# Labels and Entries
labels = [
    "Student Name:",
    "Student ID:",
    "Email:",
    "Phone Number:",
    "Course:",
    "Year Level:"
]

entries = []

for i, text in enumerate(labels):
    lbl = tk.Label(
        root,
        text=text,
        bg="#ffd6e8",
        fg="#8b005d",
        font=("Comic Sans MS", 10, "bold")
    )
    lbl.grid(row=i+1, column=0, sticky="e", padx=10, pady=6)

    ent = tk.Entry(
        root,
        width=30,
        font=("Comic Sans MS", 10),
        bg="#fff0f5"
    )
    ent.grid(row=i+1, column=1, padx=10, pady=6)

    entries.append(ent)

entry_name, entry_id, entry_email, entry_phone, entry_course, entry_year = entries

# Buttons
btn_add = tk.Button(
    root,
    text="Add Student",
    bg="#ff69b4",
    fg="white",
    font=("Comic Sans MS", 10, "bold"),
    width=15,
    command=add_student
)
btn_add.grid(row=7, column=0, pady=15)

btn_clear = tk.Button(
    root,
    text="Clear Fields",
    bg="#c77dff",
    fg="white",
    font=("Comic Sans MS", 10, "bold"),
    width=15,
    command=clear_fields
)
btn_clear.grid(row=7, column=1, pady=15)

# Student List Label
list_label = tk.Label(
    root,
    text="Student List:",
    font=("Comic Sans MS", 12, "bold"),
    bg="#ffd6e8",
    fg="#d63384"
)
list_label.grid(row=8, column=0, columnspan=2, pady=10)

# Text Area
text_area = tk.Text(
    root,
    width=80,
    height=15,
    font=("Comic Sans MS", 10),
    bg="#fff0f5"
)
text_area.grid(row=9, column=0, columnspan=2, padx=20, pady=10)

root.mainloop()