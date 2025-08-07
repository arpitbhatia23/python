distance=int(input("enter distance in km:").strip())

if distance <3:
    print("walk")
elif distance<15:
    print("bike")
elif distance>15 and distance<50:
    print("car")
else:
    print("use public transport")