'''Write a python function that checks whether a passed string is palindrome or not.'''

def test_palin(str):
    return str==str[::-1] #returns reverse of a string.

str="madam"
check=test_palin(str)
if check:
    print("True")
else:
    print("false")
