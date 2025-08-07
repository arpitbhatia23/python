
numbers=[1,-2,3,-4,5,6,-7,-8,9,10]
postive_count = 0
negavtive_count = 0
for num in numbers:
    if num <0:
        negavtive_count +=1
    else:
        postive_count +=1

print("postive count:", postive_count)
print("negavtive count:", negavtive_count)