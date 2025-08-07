string=input("Enter a string: ").strip()

reversed_string=""

for char in string:
    reversed_string=char+reversed_string

print("Reversed string:", reversed_string)