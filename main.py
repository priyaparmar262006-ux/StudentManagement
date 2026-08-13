from students import students

for student in students:
    marks = student["marks"]
    average = sum(marks) / len(marks)

    print("Name:", student["name"])
    print("Enrollment:", student["enrollment"])
    print("Marks:", student["marks"])
    print("Average:", average)
    print()
