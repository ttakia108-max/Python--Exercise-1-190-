# Printing a string without vowels
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
result = ""

for char in text:
    if char not in vowels:
        result += char

print("String without vowels:", result)