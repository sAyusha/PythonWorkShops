''' School decided to replace desks in 3 classrooms. Each desk sits 2 students. Given the number of students in each
class, print the smallest number of desk that can be purchased.
'''
class1=int(input("Enter the number of student in 1st class:"))
class2=int(input("Enter the number of student in 2nd class:"))
class3=int(input("Enter the number of student in 3rd class:"))

total_students=(class1+class2+class3)
desk=total_students/2
number=round(desk)
print("The total number of desk required is:",number)
