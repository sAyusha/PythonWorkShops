'''Write a function called show_stars(rows).If rows is 5 it should print the followig:
*
**
***
****
*****'''

def show_stars(rows):
    for i in range(rows):
        for j in range(i+1):
            print("*",end="")
        print("\n")
show_stars(5)