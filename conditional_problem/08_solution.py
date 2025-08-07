password=input("Enter your password: ").strip()

if len(password)<6:
    print("password is weak")
elif len(password)<10:
    print("password is medium")
else:
    print("password is strong")
