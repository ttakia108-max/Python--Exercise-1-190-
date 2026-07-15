# Checking if a character is a Bangla Alphabet

char = input("Enter a single character: ")

if 'অ' <= char <= '৿':
    print(char, "is a Bangla Alphabet")
else:
    print(char, "is NOT a Bangla Alphabet")