age = int(input("Enter your age: "))
day = input("Enter \"weekday\" or \"weekend\" in lowercase: ")
valid = "True"
if  age < 0:
    print("Age cannot be invalid")
    valid = "False"
if  day != "weekday" and day != "weekend":
    print("Please enter weekday or weekend")
    valid = "False"
if valid == "False":exit()

if day == "weekday":
    if age >= 65:
        print("You elder ticket price is $8")
    elif age >= 13:
        print("You adult ticket price is $11")
    else:print("You child ticket price is $6")
else:
    if age >= 65:
        print("You elder ticket price is $10")
    elif age >= 13:
        print("You adult ticket price is $14")
    else:print("You child ticket price is $8")