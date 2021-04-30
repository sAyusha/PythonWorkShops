'''WAP to find fcatorial of number using function.'''
def factorial(num):
    if num<0:
        return 'number cannot be negative.'
    elif num==1 or num==0:
        return 1
    else:
        return num*factorial(num-1)

print(factorial(5))