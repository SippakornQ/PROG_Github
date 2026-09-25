import lib

n = int(input())
numbers = []

for j in range(n):
    numbers.append(int(input()))

command = input()

if command == "sum":
    print(lib.sum(numbers))
elif command == "count":
    print(lib.count(numbers))
elif command == "max":
    print(lib.max(numbers))
elif command == "min":
    print(lib.min(numbers))
elif command == "average":
    print(lib.average(numbers))
else:
    print("invalid command")