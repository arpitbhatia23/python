pet=input("enter type of yout pet :").strip().lower()
age=int(input("enter your pet's age:"))

if pet == "dog":
    if age <2:
        print("give it puppy food")
    elif age >2:
        print("give it dog food")
elif pet == "cat":
    if age <2:
        print("give it kitten food")
    elif age >2:
        print("give it cat food")
else:
    print("we don't have food for this pet")