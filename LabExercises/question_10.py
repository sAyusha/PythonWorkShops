'''WAP to convert seconds to day , hour and minutes.'''
second=int(input('Enter the number of seconds: '))
minute=(second//60)
print(f"Total minutes for given seconds: {minute}")
hours=((second//60)//60)
print(f"total hours for given seconds: {hours}")
day=(((second//60)//60)//24)
print(f"Total day for given seconds: {day}")
