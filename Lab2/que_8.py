'''Given a three-digit number.Find sum of its digit.'''
num=int(input('Enter the three-digit number:'))
a=num//100
b=num//10%10
c=num%10
sum=(a+b+c)
print(sum)

def getSum(n):
    sum=0
    while (n!=0):
        sum=sum + int(n%10)
        n=int(n/10)
    return sum

n=659
print(getSum(n))