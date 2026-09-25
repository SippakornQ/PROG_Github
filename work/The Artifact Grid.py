line1 = input("enter first line: ").split()

rows = int(line1[0])
columns = int(line1[1])

count = 0
total_sum = 0

for _ in range(rows):
    row = input("enter the row: ").split()
    for nstr in row:
        num = int(nstr)
        if num >=10 and num <= 50 and num % 2 == 0:
            count += 1
            total_sum += num
print(count)
print(total_sum)