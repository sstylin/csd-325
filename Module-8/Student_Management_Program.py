# Student Management Program: 
# Steve Stylin@Bellevue University Module 8.2:  JSON Practice

## Requirement Summary
#This document outlines a Python program that manages a list of students stored in a JSON file. 
# The program will load student data, display it, allow the user to add a new student, and save the updated list back to the JSON file. 
# It includes error handling and user notifications.

## importing libraries

import json
import os
import tkinter as tk
from tkinter import messagebox

# Define the path to the student.json file
json_file_path = 'C:\csd\csd-325\Module-8\student.json'

# Load the student data from the JSON file
def load_students():
    try:
        with open(json_file_path, 'r') as file:
            students = json.load(file)
            return students
    except FileNotFoundError:
        print("Error: The file student.json was not found.")
        exit()
    except json.JSONDecodeError:
        print("Error: The file student.json is not a valid JSON.")
        exit()

# Print the student list
def print_students(students):
    print("Original Student List:")
    for student in students:
        print(f"{student['F_Name']} , {student['L_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")

# Append a new student to the list, first the program check if the student exit, if yes, an error message is printed. If no, the new student is add to the student.json list
def add_student(students, first_name, last_name, student_id, email):
    for student in students:
        if student['Student_ID'] == student_id:
            print(f"\nError: Student ID {student_id} already exists.")
            exit()
    new_student = {
        "F_Name": first_name,
        "L_Name": last_name,
        "Student_ID": student_id,
        "Email": email
    }
    students.append(new_student)

# Save the updated student list back to the JSON file
def save_students(students):
    try:
        with open(json_file_path, 'w') as file:
            json.dump(students, file, indent=4)
    except IOError:
        print("Error: Unable to write to the file student.json.")
        exit()

# GUI notification for saving the file depends on the user input. 
def ask_to_save():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    return messagebox.askyesno(f"\n{json_file_path} ","This file have been modified outside. Do you want to reload it?")

# Main function to execute the program
def main():
    students = load_students()
    print_students(students)

    # User input for new student details
    first_name = "Steve"
    last_name = "Stylin"
    student_id = 57852 # The student id is fictional
    email = "sstylin@bellevue.edu" # the university email is fictional

    add_student(students, first_name, last_name, student_id, email)
    print("Updated Student List:")
    print_students(students)

    if ask_to_save():
        save_students(students)
        print("Changes saved to student.json.") # The new student will be add to the file if user click on YES on the nodification GUI message
    else:
        print("No changes were saved.") # If user click NO. no change will be made on the student.json file

if __name__ == "__main__":
    main()
