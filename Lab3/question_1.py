'''Write a python function to find the Maximum of three numbers.'''
def max(a,b,c):
    if a>b and a>c:
        print("a is the maximum number.")
    elif b>a and b>c:
        print("b is the maximum number.")
    elif c>a and c>b:
        print("c is the maximum number.")
    else:
        print("number is invalid.")

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("Enter the third number:"))
max(a,b,c)