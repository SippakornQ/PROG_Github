# X = ["1234","sijdnbfd","3.13432;3l2"]
# print(X[0])

# y = "ello123456" #list[start:end:step]
# print(y[:4])
# print(y[:7])

# X = ["1234","sissd","3.13"]

# # x = "hello , jarnred"
# # x = x.split()
# # print(x)
# x = int(input())
# if x //2 == 0:
#     print("even")
# else:
#     print("odd")

# a = ["1","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32"] #have 22 item 
# for i in range(len(a)):
#     print(f"{i + 1} is a {a[i]}")

# num = [1,2,3,4,5,6,7,8,9,10]
# print(num[1:8:2])
# print(num[::2])
# print(num[::-1])
# while True:         # will true 
#     word = input("type 'again: ") #input
#     if word != "again":     #condition
#         break       #stop in py
# print("stopped")

# while True:         
#     word = input(">: ") 
#     if word == "ping":
#         print("pong")
#     elif word == "about":
#             print("PROG CLI")
#     elif word == "quit":
#         break
#     else:
#         print("unknow comman")

# num_list = []
# for i in range(3):
#             sub_list = []
#             for j in range(3):
#                 sub_list=len(range(j))
# num_list % sub_list
# print(num_list)

# number_a = [2,4,9]
# t = 0
# for number in number_a :
#     t = t + number
# print(t/len(number_a))

# number_b = [10,20,30]
# t1 = 0
# for number in number_b :
#     t1 = t1 + number
# print(t1/len(number_b))

# number_c = [1,5,9,13]
# t2 = 0
# for number in number_c :
#     t2 = t2 + number
# print(t2/len(number_c))

# def N_WORD (A,B):
#     print(f"hi my {A} and {B}")

# N_WORD("NIG","JAFE")
def biggest(numbers):
    best = numbers[0]
    for n in numbers:
        if n > best:
            best = n
    return best

print(biggest([-3, -7, -1]))