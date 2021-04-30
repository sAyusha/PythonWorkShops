'''write a python function  that accepts a string and
calculate the number of uppercase letter and lowercase letters.'''
def case_count(str):
    UPPER_CASE=0
    LOWER_CASE=0
    for s in str:
        if s.isupper():
           UPPER_CASE=UPPER_CASE+1
        elif s.islower():
           LOWER_CASE=LOWER_CASE+1
        else:
           pass
    print ("No. of Upper case characters : ", UPPER_CASE)
    print ("No. of Lower case Characters : ", LOWER_CASE)

case_count('Hi I am Ayusha Shrestha')
