def sum(x):
    total = 0
    for num in x:
        total += num
    return total

def count(x):
    total_items = 0
    for _ in x:
        total_items += 1
    return total_items

def max(x):
    biggest = x[0]
    for num in x:
        if num > biggest:
            biggest = num
    return biggest

def min(x):
    smallest = x[0]
    for num in x:
        if num < smallest:
            smallest = num
    return smallest

def average(x):
    return sum(x) / count(x)