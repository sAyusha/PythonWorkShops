'''Given three integers,print the smallest one.
(Three integers should be user input.'''
num1=3
num2=8
num3=4
if num1<num2 and num1<num3:
    print(f'smallest one is {num1}')
elif num2<num3 and num2<num1:
    print(f'smallest one is {num2}')
else:
    print(f'smallest one is {num3}')
