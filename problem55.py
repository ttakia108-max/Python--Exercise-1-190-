# Checking if a string contains only digits

text = input("Enter a string: ")

if text.isdigit():
    print(text, "contains only Digits")
else:
    print(text, "does NOT contain only Digits")