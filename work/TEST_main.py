from TEST_calculations import calculate_total
from TEST_receipt import print_receipt

prices = [20, 35, 15]
total = calculate_total(prices)
print_receipt("Guide", total)

# def calculate_total(prices): is same in upper 1-6 line
#     return sum(prices)

# def print_receipt(customer, total):
#     print(customer, "Total:", total)

# prices = [20, 35, 15]
# total = calculate_total(prices)
# print_receipt("Guide", total)