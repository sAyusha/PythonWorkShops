'''task ----- condition
weight converter-input the weight of a person in either kg or lbs.
If the person provides his/her weight in kg convert it into lbs
else convert it into kg.'''
weight=int(input("Enter the weight of a person:"))
unit=input("Enter the unit of weight:")
if unit=='kg':
    weight_inlbs=weight*0.45359237
    print(f'the weight of a person in lbs is {weight_inlbs}')
elif unit=='lbs':
    weight_inkg=weight*2.20462262
    print(f'the weight of a person in kg is {weight_inkg}')
