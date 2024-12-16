import tkinter as tk
from tkinter import messagebox
import sqlite3

# Create Database or Connect to Existing Database
def create_connection():
    conn = sqlite3.connect("student_management.db")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    age INTEGER,
                    grade TEXT)''')
    conn.commit()
    return conn

# Add Student
def add_student():
    name = entry_name.get()
    age = entry_age.get()
    grade = entry_grade.get()

    if not name or not age or not grade:
        messagebox.showerror("Input Error", "All fields are required")
        return

    try:
        age = int(age)
    except ValueError:
        messagebox.showerror("Input Error", "Age must be a number")
        return

    conn = create_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", (name, age, grade))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Student added successfully")
    clear_fields()
    display_students()

# Clear Input Fields
def clear_fields():
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_grade.delete(0, tk.END)

# Display Students in Listbox
def display_students():
    listbox_students.delete(0, tk.END)
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    for row in rows:
        listbox_students.insert(tk.END, f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Grade: {row[3]}")
    conn.close()

# Delete Student
def delete_student():
    selected = listbox_students.curselection()
    if not selected:
        messagebox.showerror("Selection Error", "No student selected")
        return

    student_id = listbox_students.get(selected).split(",")[0].split(":")[1].strip()
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Student deleted successfully")
    display_students()

# Update Student
def update_student():
    selected = listbox_students.curselection()
    if not selected:
        messagebox.showerror("Selection Error", "No student selected")
        return

    student_id = listbox_students.get(selected).split(",")[0].split(":")[1].strip()
    name = entry_name.get()
    age = entry_age.get()
    grade = entry_grade.get()

    if not name or not age or not grade:
        messagebox.showerror("Input Error", "All fields are required")
        return

    try:
        age = int(age)
    except ValueError:
        messagebox.showerror("Input Error", "Age must be a number")
        return

    conn = create_connection()
    cur = conn.cursor()
    cur.execute("UPDATE students SET name=?, age=?, grade=? WHERE id=?", (name, age, grade, student_id))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Student updated successfully")
    clear_fields()
    display_students()

# Set up main window
root = tk.Tk()
root.title("Student Management System")

# Create Input Fields
label_name = tk.Label(root, text="Student Name:")
label_name.grid(row=0, column=0, padx=10, pady=10)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=10)

label_age = tk.Label(root, text="Age:")
label_age.grid(row=1, column=0, padx=10, pady=10)
entry_age = tk.Entry(root)
entry_age.grid(row=1, column=1, padx=10, pady=10)

label_grade = tk.Label(root, text="Grade:")
label_grade.grid(row=2, column=0, padx=10, pady=10)
entry_grade = tk.Entry(root)
entry_grade.grid(row=2, column=1, padx=10, pady=10)

# Create Buttons
button_add = tk.Button(root, text="Add Student", command=add_student)
button_add.grid(row=3, column=0, padx=10, pady=10)

button_update = tk.Button(root, text="Update Student", command=update_student)
button_update.grid(row=3, column=1, padx=10, pady=10)

button_delete = tk.Button(root, text="Delete Student", command=delete_student)
button_delete.grid(row=3, column=2, padx=10, pady=10)

# Listbox to display students
listbox_students = tk.Listbox(root, width=50, height=10)
listbox_students.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

# Initialize the display with students from the database
display_students()

# Start the Tkinter event loop
root.mainloop()
