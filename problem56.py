# Checking first letter of a word

word = input("Enter a word: ")

first_char = word[0].lower()

if first_char in ['a', 'e', 'i', 'o', 'u']:
    print(first_char, "is a Vowel")
elif first_char.isalpha():
    print(first_char, "is a Consonant")
else:
    print("Invalid input!")