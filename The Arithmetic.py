weight = float(input("enter weight: "))
height = float(input("enter height: "))

height_in_metres = height / 100
BMI = weight / (height_in_metres ** 2)
print(f"{BMI:.2f}")