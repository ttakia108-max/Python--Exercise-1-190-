# Converting half of the string to Uppercase
text = input("Enter text: ")

half_text = text[:len(text)//2]
upper_text = half_text.upper()

print("Uppercase Text:", upper_text)