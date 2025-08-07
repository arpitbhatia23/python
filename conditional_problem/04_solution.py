fruit="banana"
color= input("enter color of banana:").strip().lower()
if fruit=="banana":

    if color=="green":
         print("banana is unripe")
    elif color=="yellow":
        print("banana is ripe")
    elif color=="brown":
        print("banana is overripe")
    else:
        print("this color of banana not exit")

else:
    print("furit didn't exit in my data base")

