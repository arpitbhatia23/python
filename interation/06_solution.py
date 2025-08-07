number=int(input("enter a number"))
factnum=number
factorial=1

while number>=1:
    factorial *=number
    number -=1

print(f"factorial of {factnum} is {factorial}")