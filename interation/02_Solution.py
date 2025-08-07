number=int(input("Enter a number: "))

sum_even=0

for i in range(1,number + 1):
    if i%2==0:
        sum_even+=1
print("The sum of even numbers from 1 to", number, "is:", sum_even)
    