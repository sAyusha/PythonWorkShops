'''Write a Python function that accepts a string and
calculate the number of upper case letters and lower case letters.'''
def case_count(str):
    UPPER=0
    LOWER=0
    for s in str:
        if s.isupper():
           UPPER=UPPER+1
        elif s.islower():
           LOWER=LOWER+1
        else:
           pass
    print ("No. of Upper case characters : ", UPPER)
    print ("No. of Lower case Characters : ", LOWER)

case_count('Hi I am Ayusha Shrestha')