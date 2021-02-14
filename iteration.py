# for i in range(10):
#     print("=")

# for i in range(10):
#     print(i)

# for i in range(10):
#     print("="+str(i+1)+"=")

# for i in range(4):
#     for j in range(4):
#         print(i + j, end=" ")
#         print()

# for i in range(6):
#     n1 = i + 1
#     for j in range(6):
#         n2 = j + 1
#         print(n1, n2)
#1부터 6까지의 눈금이 있는 주사위를 두 번 던져서 나온 숫자들

# for i in range(6):
#     n1 = i + 1
#     for j in range(6):
#         n2 = j + 1
#         n = n1 + n2
#         if n % 4 == 0:
#             print(n1, n2)
#주사위를 두 번 던져서 나온 숫자들의 합이 4의 배수가 되는 경우만 구해야 한다

# n = 5
# sum = 0
# for i in range(n):
#     sum = sum+(i+1)
# print(sum)
#1부터 5까지의 합

for j in range(10):
    sum = 0
    for i in range(j+1):
        sum = sum + (i+1)
    print(sum)