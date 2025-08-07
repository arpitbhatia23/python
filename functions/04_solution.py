import math
def circle_stats(r):
    area=math.pi* r**2
    circum=2*math.pi*r
    return area,circum

a,c=circle_stats(5)

print(f"area :{int(a)} circumference :{int(c)}")

