'''If name is less than 3 characters long - name must be at least 3 characters
otherwise if it's more than 50 characters - name must be maximum of 50 charcaters
otherwise - name looks good.'''
name=input('enter the name:')
if len(name)<3:
    print("name must be at least of 3 characters.")
elif len(name)>50:
    print("the name must be maximum of 50 characters.")
else:
    print("name looks good.")