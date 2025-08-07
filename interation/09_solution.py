items=["apple","apple","banana","cherry","date","elderberry"]

unique_items=set()

for item in items:
    if item in unique_items:
        print(f"{item} is dupllicate")
        break
    unique_items.add(item)


