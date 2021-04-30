'''write a python function that takes a number as a parameter and check the number is prime or not.'''

def test_prime(num):
    if num==1:
        return False
    elif num==2:
        return True
    else:
        for i in range(2,num):
            if num % i == 0:
                return False
        return True

num=int(input("enter a number:"))
print(test_prime(num))