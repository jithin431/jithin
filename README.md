
Title:
Student Management System (SMS) using Tkinter and SQLite

Abstraction:
This program is a graphical user interface (GUI)-based student management system that allows users to interact with student records stored in an SQLite database.
Through the interface, users can perform CRUD (Create, Read, Update, Delete) operations on student data. The system enables easy management of student information, 
including their name, age, and grade, with real-time updates in the list of students.

Overview:
The Student Management System (SMS) provides a simple yet effective solution for managing student data.
It leverages Python's Tkinter library for the GUI and sqlite3 for database management. The program facilitates the following operations:

Add Student: Allows the user to input new student details.
Update Student: Lets the user modify existing student records.
Delete Student: Enables the user to remove a student from the database.
View Students: Displays a list of all students stored in the database.
The application validates user inputs (e.g., ensuring age is a number), provides error messages when needed, and updates the list of students in real-time whenever any operation is performed.

Features:
Database Integration with SQLite:

Uses SQLite for storing and managing student records in a local database (student_management.db).
The database contains a students table with columns for id, name, age, and grade.
Add Student:

Allows the user to enter a student's name, age, and grade.
Validates input to ensure all fields are filled and that the age is a valid integer.
Adds the new student to the database upon validation.
Update Student:

The user can select a student from the list to update their details.
After entering updated information, the system updates the student's record in the database.
Validation ensures that the age is a number and all fields are filled.
Delete Student:

The user can select a student from the list to delete.
Deletes the selected student from the database and updates the list of students in the UI.
Display Students:

The student records are displayed in a scrollable listbox that includes each student's id, name, age, and grade.
The list is refreshed automatically after every add, update, or delete operation.
Error Handling and Input Validation:

The system ensures that all input fields are filled before adding or updating a student.
Displays error messages for invalid input, such as when the age is not a number or when no student is selected for deletion or update.
User-Friendly Interface:

A clear and intuitive Tkinter-based GUI, including labels, entry fields, buttons, and a listbox.
Error messages and success notifications are shown via pop-up messageboxes, ensuring user interaction is simple and clear.
Clear Input Fields:

After each operation (adding or updating a student), the input fields are cleared, allowing for new data entry.
Persistent Storage:

Student data is stored persistently in a local SQLite database, so records remain intact between sessions
