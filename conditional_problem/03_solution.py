
score=int(input("enter your grade :"))
if score>100:
    print(" grade is not accepetable")
    exit()
if score>=90:
    grade="A"

elif score>=80:
    grade="B"

elif score>=70:
    grade="C"

elif score>=60:
    grade="D"
else:
    grade="F"

print("your grade is ", grade)