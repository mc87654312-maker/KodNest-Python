# employees = [
#     {"employee_id": "E101", "name": "Asha", "department": "Development"},
#     {"employee_id": "E102", "name": "Ravi", "department": "Testing"},
#     {"employee_id": "E103", "name": "Meera", "department": "Support"}
# ]

# employee_by_id = {}

# for employee in employees:
#     employee_id = employee["employee_id"]
#     employee_by_id[employee_id] = employee
# required_id = "E102"

# if required_id in employee_by_id:
#     employee = employee_by_id[required_id]

#     print(employee["name"])
#     print(employee["department"])
# else:
#     print("Employee not found")    

# def group_students(students):
#     students_by_course = {}
#     for name, course in students:
#         if course not in students_by_course:
#             students_by_course[course] = []
#         students_by_course[course].append(name)
#     return students_by_course

def group_students(students):
    students_by_course = {}
    for name, course in students:
        if course not in students_by_course:
            students_by_course[course] = []
        students_by_course[course].append(name)
    return students_by_course


n = int(input())
students = []
for _ in range(n):
    name, course = input().split()
    students.append((name, course))

students_by_course = group_students(students)
for course, names in students_by_course.items():
    print(course + ": " + " ".join(names))