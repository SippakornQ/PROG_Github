items = int(input("items: "))
amount_paid = float(input("amount_paid: "))

if items >5:
    if amount_paid >=500:
        print("Discount")
    else:
        print("No Discount")
else:
    print("Normal")
