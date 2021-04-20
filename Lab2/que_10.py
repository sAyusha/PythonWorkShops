'''WAP to sum of three integers. However,if two values are equal sum will be zero.'''
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number: "))
if a==b or b==c or a==c:
    print("sum will be zero.")
else:
    print(f"the sum is {a+b+c}")