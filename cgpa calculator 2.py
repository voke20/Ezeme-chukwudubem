print("GPA Calculator for 8 courses (use letter grades A, B, C, D, or F and enter course units)")
letter_points = {'A':5.0, 'B':4.0, 'C':3.0, 'D':2.0, 'F':0.0}
total_points = 0.0
total_units = 0.0

for i in range(8):
    course = input("Course " + str(i+1) + " name: ")
    
    units_str = input(course + " units (e.g., 3): ")
    if units_str.isdigit():
        units = float(units_str)
    else:
        print("Invalid units, counted as 0")
        units = 0.0
    
    grade = input(course + " grade (A-F): ")
    grade = grade.strip().upper()
    if grade in letter_points:
        points = letter_points[grade]
    else:
        print("Invalid grade, counted as F")
        points = letter_points['F']
  
    total_points += points * units
    total_units += units


if total_units > 0:
    gpa = total_points / total_units
    print("Your weighted GPA is", round(gpa, 2))
else:
    print("No valid units entered, cannot compute GPA.")