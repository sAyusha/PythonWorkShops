'''WAP which accepts marks of four subjects and display total marks, percentage and grade.
Hint: more than 70% --> distinction, more than 60% --> firts, more tham 40% --> pass, less than 40% --> fail.'''
s1=int(input('enter the 1st subject:'))
s2=int(input('enter the 2nd subject:'))
s3=int(input('enter the 3rd subject:'))
s4=int(input('enter the 4th subject:'))
total_marks=s1+s2+s3+s4
percent = ((total_marks)/400)*100
if percent >= 70:
    print('distinction')
elif percent>=60:
    print('first division')
elif percent>=40:
    print('pass')
elif percent<=40:
    print('fail')
else:
    print('invalid result')