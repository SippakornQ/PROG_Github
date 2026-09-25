import random
num_list = []

for i in range(3):
    sub_list = []
    for j in range(3):
        sub_list.append(random.randint(1,100))
    num_list.append(sub_list)
print(num_list)
