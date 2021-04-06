'''game finding a secret number within 3 attempts using while loop.'''
num=5
counter=1
while counter<=3:
    guess=int(input('Enter the valid guess:'))
    counter=counter+1
    if guess==num:
        print('congratulations you have won!')
    else:
        print('try again!!')


