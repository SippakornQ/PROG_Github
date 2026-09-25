from HW_calculations import calulate_total
from HW_receipt import print_receipt

prices = [20,35,15]
total = calulate_total(prices)
print_receipt("Guide",total)