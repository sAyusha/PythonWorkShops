'''You live 4 miles from university.The bus drives at 25mph but spends 2 minutes at each of the 10 stops.
How long will the bus journey takes?You jog the first mile at 7mph;the run the next two at 15mph;
 before jogging tha last  at 7mph again.Will this be quicker or slower than the bus?'''

living_miles_apart=4
bus_velocity=25
time_taken=((living_miles_apart/bus_velocity)*60)

#2 minutes at each stop.
time_spend=20
total_bus_time=time_taken + time_spend
print(f"total time taken by the bus is{total_bus_time}")

#run to university.
jog_1=((1/7)*60)
jog_2=((2/15)*60)
jog_3=((1/7)*60)
total_walk_time=jog_1+jog_2+jog_3
print(f"total time taken by walk is{total_walk_time}")

if (total_bus_time<total_walk_time):
    print("taking bus is quicker than running")
else:
    print("taking bus is slower than running")