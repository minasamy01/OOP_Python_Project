# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 12:21:24 2024
@author: Mina
"""

import random
class User:
    def __init__(self, name, user_id, username, password, role):
        self.__name = name
        self.__user_id = user_id
        self.__username = username
        self.__password = password
        self.__role = role

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def get_name(self):
        return self.__name

    def get_user_id(self):
        return self.__user_id

    def get_role(self):
        return self.__role

    def __repr__(self):
        return f'User({self.__name}, {self.__user_id}, {self.__username}, {self.__role})'

class Student(User):
    def __init__(self, name, user_id, username, password):
        super().__init__(name, user_id, username, password, "student")
        self.courses = []
        self.assignments = []

class Doctor(User):
    def __init__(self, name, user_id, username, password):
        super().__init__(name, user_id, username, password, "doctor")

class Course:
    def __init__(self, name, code, doctor, assignments):
        self.__name = name
        self.__code = code
        self.__doctor = doctor
        self.__assignments = assignments
        self.students = []

    def get_name(self):
        return self.__name

    def get_code(self):
        return self.__code

    def get_doctor(self):
        return self.__doctor

    def get_assignments(self):
        return self.__assignments

    def __repr__(self):
        return f'Course({self.__name}, {self.__code}, {self.__doctor})'

def create_dummy_data():
    doctors = [
        Doctor("Ali", "d001", "d001", "d001"),
        Doctor("Mostafa", "d002", "d002", "d002"),
        Doctor("Hani", "d003", "d003", "d003"),
        Doctor("Mohamed", "d004", "d004", "d004"),
        Doctor("Ashraf", "d005", "d005", "d005"),
        Doctor("Samy", "d006", "d006", "d006"),
        Doctor("Morad", "d007", "d007", "d007"),
        Doctor("Sayed", "d008", "d008", "d008"),
        Doctor("Hussien", "d009", "d009", "d009"),
    ]

    courses = [
        Course("Prog 1", "CS111", "Samy", 3),
        Course("Prog 2", "CS112", "Morad", 3),
        Course("Math 1", "CS123", "Ashraf", 3),
        Course("Math 2", "CS333", "Hani", 4),
        Course("Prog 3", "CS136", "Sayed", 3),
        Course("Stat 1", "CS240", "Hussien", 3),
        Course("Stat 2", "CS350", "Morad", 3),
    ]

    students = [
        Student("Hussien Samy", "00102345", "s00102345", "s00102345"),
        Student("Ashraf Sayed", "00204690", "s00204690", "s00204690"),
        Student("Mostafa Hussien", "00307035", "s00307035", "s00307035"),
        Student("Ali Mohamed", "00409380", "s00409380", "s00409380"),
        Student("Hani Sayed", "00501725", "s00501725", "s00501725"),
    ]

    course_enrollments = {
        "00102345": ["CS111", "CS112", "CS333", "CS136", "CS240", "CS350"],
        "00204690": ["CS111", "CS112", "CS123", "CS333", "CS136", "CS240", "CS350"],
        "00307035": ["CS112", "CS123", "CS333", "CS136"],
        "00409380": ["CS111", "CS112", "CS123", "CS333", "CS136", "CS350"],
        "00501725": ["CS111", "CS112", "CS123", "CS333", "CS136", "CS240"],
    }

    for student in students:
        student_courses = course_enrollments.get(student.get_user_id(), [])
        for course_code in student_courses:
            for course in courses:
                if course.get_code() == course_code:
                    student.courses.append(course)
                    course.students.append(student)

    users = students + doctors

    return users, courses

def login(users):
    username = input("Enter username: ")
    password = input("Enter password: ")
    for user in users:
        if user.get_username() == username and user.get_password() == password:
            print(f"Welcome, {user.get_name()}. You are logged in.")
            return user
    print("Invalid username or password.")
    return None

def list_courses(user):
    if user.courses:
        print("My Courses list:")
        for idx, course in enumerate(user.courses, start=1):
            print(f"{idx}) Course {course.get_name()} - Code {course.get_code()}")
    else:
        print("You are not registered in any courses.")

def view_course(user):
    list_courses(user)
    choice = int(input("Which course to view? [1 - {}]: ".format(len(user.courses))))
    if 1 <= choice <= len(user.courses):
        course = user.courses[choice - 1]
        print(f"Course {course.get_name()} with Code {course.get_code()} - taught by Doctor {course.get_doctor()}")
        print(f"Course has {course.get_assignments()} assignments")
        for i in range(course.get_assignments()):
            submitted = "submitted" if i < len(user.assignments) else "NOT submitted"
            print(f"Assignment {i + 1} {submitted} NA / {random.randint(20, 50)}")
    else:
        print("Invalid course selection.")

def submit_assignment(course, user):
    view_course(user)
    assignment_number = int(input("Which assignment to submit? [1 - {}]: ".format(course.get_assignments())))
    if 1 <= assignment_number <= course.get_assignments():
        solution = input("Enter the solution (no space): ")
        user.assignments.append((course.get_code(), assignment_number, solution))
        print("Assignment submitted successfully!")
    else:
        print("Invalid assignment number.")

def view_grades_report(user):
    print("Grades Report:")
    for course in user.courses:
        total_assignments = course.get_assignments()
        submitted_assignments = len([assignment for assignment in user.assignments if assignment[0] == course.get_code()])
        print(f"Course code {course.get_code()}")
        print(f"Total submitted {submitted_assignments} assignments")
        print(f"Grade {random.randint(0, 25)} / {random.randint(50, 100)}")

def logged_in_menu(user):
    while True:
        print("\nPlease make a choice:")
        print("1 - Register in Course")
        print("2 - List My Courses")
        print("3 - View Course")
        print("4 - Grades Report")
        print("5 - Log out")

        choice = input("Enter Choice: ")

        if choice == '1':
            pass  # Functionality to be added
        elif choice == '2':
            list_courses(user)
        elif choice == '3':
            view_course(user)
            while True:
                print("\nPlease make a choice:")
                print("1 - Unregister from Course")
                print("2 - Submit solution")
                print("3 - Back")
                choice = input("Enter Choice: ")
                if choice == '1':
                    pass  # Functionality to be added
                elif choice == '2':
                    submit_assignment(user.courses[0], user)  # Fix this to select the correct course
                elif choice == '3':
                    break
        elif choice == '4':
            view_grades_report(user)
        elif choice == '5':
            print("Logged out successfully.")
            break

def sign_up(users):
    name = input("Enter your name: ")
    user_id = input("Enter your ID: ")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    role = "student"
    
    for user in users:
        if user.get_username() == username or user.get_user_id() == user_id:
            print("Username or ID already exists. Please try again.")
            return None
    
    new_user = Student(name, user_id, username, password)
    users.append(new_user)
    print("Sign-up successful! You can now log in.")
    return new_user

def main():
    users, courses = create_dummy_data()
    while True:
        print("\nPlease make a choice:")
        print("1 - Login")
        print("2 - Sign up")
        print("3 - Shutdown system")

        choice = input("Enter Choice: ")

        if choice == '1':
            user = login(users)
            if user:
                logged_in_menu(user)
        elif choice == '2':
            sign_up(users)
        elif choice == '3':
            print("System shutdown. Goodbye!")
            break

if __name__ == "__main__":
    main()

