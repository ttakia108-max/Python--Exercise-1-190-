# Finding vowel frequency in a string
text = input("Enter a string: ").lower()

freq = {}

for char in text:
    if char in "aeiou":
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

print("Vowel Frequencies:")

for char, count in freq.items():
    print(f"'{char}' : {count}")