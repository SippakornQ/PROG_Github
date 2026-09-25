line1 = input("enter the line: ").split()
rows = int(line1[0])
columns = int(line1[1])
target = int(line1[2])

vulnerable_count = 0
max_vulnerable_sum = 0

for i in range(rows):
    row_tokens = input("enter the row: ").split()
    row_sum = 0
    
    for token in row_tokens:
        row_sum += int(token)
        
    if row_sum >= target:
        vulnerable_count += 1
        if row_sum > max_vulnerable_sum:
            max_vulnerable_sum = row_sum

print(vulnerable_count)
print(max_vulnerable_sum)