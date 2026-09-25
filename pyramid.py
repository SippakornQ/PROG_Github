S = (input("enter your character: "))
M = int(input("enter your integer number: "))

for i in range(1,M+1):
    for j in range(i):
        print(S ,end = "")
    print()
