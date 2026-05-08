mark = int(input("Enter grade precentage : "))

if mark >= 90:
    grade = "A"
elif mark >= 80:
    if mark >= 87:
        grade = "B+"
    elif mark < 83:
        grade = "B-"
    else:
        grade = "B"

elif mark >= 70:
    grade = "C"
elif mark >= 60:
    grade = "D"
elif mark < 60:
    grade = "B"

print(f"Grade : {grade}")