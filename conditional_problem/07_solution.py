order_size=input("Enter the order size: ").strip().lower()
extra_Shot=input("Do you want an extra shot? (yes/no): ")

if extra_Shot =="yes":
    coffee=order_size + " cofffe with an extra shot of espresso"
else:
    coffee=order_size + " coffee"

print("Your order is: " + coffee)
