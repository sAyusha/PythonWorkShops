'''Given the integer N- the number of minutes that is passed since midnight-How many hours ans minutes are
displayed on 24h digital clock.'''
N=int(input('Enter the minute passed since midnight:'))
hours=(N//60)
minute=(N%60)
print(f'the time is: {hours}hr {minute} min')


