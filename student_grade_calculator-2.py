# Student Grade Calculator

name = input("Enter student's name: ")

mark1 = float(input("Enter marks for Subject 1: "))
mark2 = float(input("Enter marks for Subject 2: "))
mark3 = float(input("Enter marks for Subject 3: "))

total = mark1 + mark2 + mark3
average = total / 3

if 80 <= average <= 100:
    grade = "A+"
elif 70 <= average < 80:
    grade = "A"
elif 60 <= average < 70:
    grade = "B"
elif 50 <= average < 60:
    grade = "C"
else:
    grade = "F"

print(f"\nStudent Name: {name}")
print(f"Total Marks: {total:g}")
print(f"Average: {average:.2f}")
print(f"Grade: {grade}")
