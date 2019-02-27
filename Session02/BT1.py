weight = int(input("Nhap vao can nang :"))
height = float(input("Nhap vao chieu cao :"))
BMI = weight / (height * height)
print(BMI)
if BMI < 16:
    print("Severely underweight")
elif BMI < 18.5:
    print("Underweight")
elif BMI < 25:
    print("Normal")
elif BMI < 30:
    print("Overweight")
else:
    print("Obese")
