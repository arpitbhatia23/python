weather=input("Enter the weather (sunny, rainy, snowy): ").strip().lower()

if weather == "sunny":
    print("go for a walk")
elif weather =="rainy":
    print("read a book")
elif weather == "snowy":
    print("build a snowman")
else:
    print("stay indoors")