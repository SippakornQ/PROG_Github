power = float(input("enter your POWER: "))
key = input("enter your key: ")

if power >= 50:
    if key == "gold":
        print("TREASURE")
    else:
        print("NEED KEY")
else:
    print("LOCKED")