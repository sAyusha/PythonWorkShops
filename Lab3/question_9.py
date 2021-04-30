'''WAP that checks whether the passed string is palindrome eor not.'''
def test_palin(str):
    return str==str[::-1] #reverse the function
str="madam"
check=test_palin(str)
if check:
    print(True)
else:
    print(False)