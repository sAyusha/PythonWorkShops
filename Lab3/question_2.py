'''write a function called fizz_buzz that takes a number.
If the number is divisible by 3, it should return "fizz"
If the number is divisible by 5, it should return "buzz"
If it is divisible by both 3 and 5, it should return "fizzbuzz"
Otherwise, it should return  the same number.'''

def Fizz_Buzz(num):
    if num%3==0 and num%5==0:
        print("FizzBuzz")
    elif num%5==0:
        print("Buzz")
    elif num%3==0:
        print("Fizz")
    else:
        print("nothing")

num=int(input("Entetr the number:"))
Fizz_Buzz(num)