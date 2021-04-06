'''If temp is greater than 30,it's a hot day
otherwise it it's less than 10,it's a cold day;
otherwise it's neither cold nor hot.'''
temp=float(input('Enter the temperature:'))
if temp>30:
    print('it is a hot day.')
elif temp<10:
    print('it is a cold day.')
else:
    print('it is neither cold nor hot day.')