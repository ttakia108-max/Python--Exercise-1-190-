# Printing words longer than 5 characters
text = input("Enter a sentence: ")

words = text.split()

for word in words:
 if len(word) > 5:
  print(word)