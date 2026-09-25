name = str(input("Your order : "))
price = float(input("Price : "))
Quantity = int(input("Quantity : "))

subtotal = price*Quantity
VAT = subtotal*0.07
total = subtotal + VAT

print(f"{'Result':=^30}")

print(f"{"Item":<10} : {name}")

print(f"{"Price":<10} : {price:.2f} Baht")

print(f"{"Quantity":<10} : {Quantity}")

print("-"*30)

print(f"{"Subtotal":<10} : {subtotal:.2f} Baht")

print(f"{"VAT 7%":<10} : {VAT:.2f} Baht")

print(f"{"Total":<10} : {total:.2f} Baht")

print("="*30)