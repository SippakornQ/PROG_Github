number = [1,2,3,4,5,6,7,8,9,10,11]

total_odd = 0
total_even = 0

for num in number:
    if num %2 == 0:
        total_even += 1
    else:
        total_odd += 1
print(f"total even is: {total_even}")
print(f"total_odd is: {total_odd}")
