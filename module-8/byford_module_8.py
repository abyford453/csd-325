"""
Title: byford_module_8.py
Author: Drew Byford
Course: CSD-325
Assignment: Module 8
Description:
This program reads student information from a JSON file,
displays the original student list, adds a new student,
displays the updated list, and writes the updated student
information back to the JSON file.
"""

import json


def print_students(student_list):
    """Print each student's name, ID number, and email address."""

    for student in student_list:
        print(
            f"{student['L_Name']}, {student['F_Name']} : "
            f"ID = {student['Student_ID']} , "
            f"Email = {student['Email']}"
        )


# Open the JSON file and load the student records into a Python list.
with open("Student.json", "r") as student_file:
    students = json.load(student_file)


# Notify the user that the original student list will be displayed.
print("\n--- Original Student List ---")

# Display all original students.
print_students(students)


# Create a new student record.
new_student = {
    "F_Name": "Drew",
    "L_Name": "Byford",
    "Student_ID": 86753,
    "Email": "dbyford@gmail.com"
}


# Add the new student to the student list.
students.append(new_student)


# Notify the user that the updated student list will be displayed.
print("\n--- Updated Student List ---")

# Display the updated student list.
print_students(students)


# Write the updated student list back to the JSON file.
with open("Student.json", "w") as student_file:
    json.dump(students, student_file, indent=4)


# Notify the user that the JSON file has been updated.
print("\nThe Student.json file has been updated.")