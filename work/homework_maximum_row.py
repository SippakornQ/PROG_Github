numbers = [[5, 10, 15],[20, 3, 7],[8, 12, 10],[30, 5, 2]]

max_sum = 0
for row in numbers:
    X = sum(row)
    if X > max_sum:
        max_sum = X
print(f"max sum of row is :{max_sum}")
