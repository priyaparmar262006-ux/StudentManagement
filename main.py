from students import students


def grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"


name = input("Enter student name: ")

if name.strip() == "":
    print("Student name cannot be empty")
else:
    found = False

    for student in students:
        if student["name"].lower() == name.lower():
            marks = student["marks"]
            average = sum(marks) / len(marks)

            print("Name:", student["name"])
            print("Enrollment:", student["enrollment"])
            print("Marks:", student["marks"])
            print("Average Marks:", average)
            print("Grade:", grade(average))

    if not found:
        print("Student not found")
