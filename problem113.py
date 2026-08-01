# Replacing spaces with underscores
text = input("Enter a sentence: ")
new_text = ""

for char in text:
    if char == ' ':
        new_text += '_'
    else:
        new_text += char

print("New sentence:", new_text)