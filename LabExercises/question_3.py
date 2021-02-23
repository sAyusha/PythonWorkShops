#N students take K apple and distribute them among each other evenly.
#The remaining undivisible part remain in basket, how many apples do each individul gets.
N=int(input('Enter the number of students'))
K=int(input('Enter number of apples'))
apple=K//N
remaining_apple=K-(apple*N)
print('total apple per student:',apple)
print('apples remaining in basket:',remaining_apple)