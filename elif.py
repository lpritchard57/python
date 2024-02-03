#Ask for the student's grade
your_grade = int(input("Enter your grade: ")) 

#Check if grade is less than 60
if your_grade < 60:
    print("F") #Grade is an F if under 60
#Check if grade is less than 70
elif your_grade < 70:
    print("D") #Grade is a D if between 60 and 69
#Check if grade is less than 80
elif your_grade < 80:
    print("C") #Grade is a C if between 70 and 79
#Check if grade is less than a 90
elif your_grade < 90:
    print("B") #Grade is a B if between 80 and 89
else:
    print("A") #Any grade 90 or higher is an A