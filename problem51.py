marks=float(input("Enter your marks(0-100):"))
if marks<0 or marks >100:
	print("invalid marks entered!")
elif marks>=85:
	print("grade: A+")
elif marks>=80:
	print("grade:A+")
elif marks>=70:
	print("grade:A")
elif marks>=60:
	print("grade:A-")
elif marks>=50:
	print("grade:B")
elif marks>=40:
	print("grade:C")
elif marks>=33:
	print("grade:D")
else:
	print("grade:F (Fail)")