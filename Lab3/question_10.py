'''accept a string from user and display only those characters which are present in even index.'''
def even_index(str):
    for i in range(0,6,2):
        print("even index:",str[i])
str=input("enter a string:")
print("display only even index characters:")
(even_index(str))
