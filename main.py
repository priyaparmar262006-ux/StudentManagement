from students import students

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
            print("Average:", average)

            found = True

    if not found:
        print("Student not found")
