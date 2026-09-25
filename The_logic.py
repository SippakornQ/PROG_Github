length = float(input("enter length: "))
material = input("enter material: ")

x = (length < 2.5) and (material in ["bronze", "copper", "silver"])
print(x)