# 1. Create a list of 5 student names and print all names.


students = ["Kritika", "Harshita", "Aprajita", "Milee", "Nilakshi"]

print(" Student Names:")
for student in students:
    print( student)


# 2. Add one new student name to the list.    


students = ["Kritika", "Harshita", "Aprajita", "Milee", "Nilakshi"]

students.append("Shivangi")

print("Updated Student List:")
for student in students:
    print( student)


# 3. Create a tuple of 5 city names and print the second city.    


cities = ("Varanasi", "Gorakhpur", "Mumbai", "Lucknow", "Jaipur")

print("Second City:", cities[1])


# 4. Create a set of 5 course names and add one new course.


courses = {"Python", "Java", "C++", "Web Development", "Data Science"}

courses.add("Machine Learning")
print(" Updated Course List:")

for course in courses:
    print( course)


# 5. Create a dictionary for one student with name, branch, batch, and marks.    


student = {
    "name": "Kritika",
    "branch": "Computer Science",
    "batch": "2026",
    "marks": 87
}

print(" Student Details")
print("Name   :", student["name"])
print("Branch :", student["branch"])
print("Batch  :", student["batch"])
print("Marks  :", student["marks"])


# 6. Print the student dictionary in a readable format.


student = {
    "name": "Kritika",
    "branch": "Computer Science",
    "batch": "2026",
    "marks": 92
}

print("╔══════════════════════════════╗")
print("║       STUDENT REPORT         ║")
print("╚══════════════════════════════╝")

print(f"Name      : {student['name']}")
print(f"Branch    : {student['branch']}")
print(f"Batch     : {student['batch']}")
print(f"Marks     : {student['marks']}/100")

if student["marks"] >= 90:
    print(" Performance: Excellent")
elif student["marks"] >= 75:
    print(" Performance: Very Good")
elif student["marks"] >= 60:
    print(" Performance: Good")
else:
    print(" Performance: Needs Improvement")

print("\n Keep Learning and Keep Growing! ")