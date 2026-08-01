# Printing text without digits

text = input("Enter a string with numbers: ")

for char in text:
    if not char.isdigit():
        print(char, end="")