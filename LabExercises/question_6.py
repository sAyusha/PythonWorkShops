'''A person's body mass index (BMI) is defined as:
BMI=mass in kg/(height in m)^2.'''
body_mass=float(input('Enter the body mass in kg:')) #takes in body mass of person.
height=float(input('Enter the height in meter:')) #takes in height of person.
BMI=(body_mass/(height**2)) #using formula of body mass index.
print(f"the body mass index is{BMI}") #prints the body mass index of person.
