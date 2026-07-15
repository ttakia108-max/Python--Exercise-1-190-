age = int(input("Enter your age: "))

if age >= 18 and age <= 30:
    print("You are eligible to apply for a government job.")
elif age < 18:
    years_left = 18 - age
    print("You are NOT eligible to apply.")
    print("Please wait for", years_left, "more years.")
else:
    print("You are NOT eligible to apply.")
    print("You have crossed the maximum age limit.")