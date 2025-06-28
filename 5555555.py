# a = [1, 4, 7, 12, 16, 21, 35, 45, 67, 78]
# print([*filter(lambda x: x%2==0, a)])
# позиция   кол во  цена
# хлеб 7 5    мясо 2 15    соль 12 3
# def marg(*a, b = 10):
#     s = sorted(a, key = lambda x: x[2])
#     s.reverse()
#     n = []
#     i = 0
#     while b > 0:
#         if i == len(s):
#             break
#         if b > s[i][1]:
#             b -= s[i][1]
#             n.append([s[i][0], s[i][1]])
#         else:
#             n.append([s[i][0], b])
#             b = 0
#         i += 1
#     return n
# print(marg(["хлеб", 7, 5], ["мясо", 2, 15], ["соль", 12, 3], ["крупа", 10, 4]))



# 6534575
# s = 6534575
# while s > 0:
#     print(s%10, end = "")
#     s = s//10

# def chi(n):
#     print(n%10, end = "")
#     if n > 9:
#         chi(n//10)
# chi(6534575)


# def prostoe(n, m = 2):
#     if n%m == 0:
#         return False
#     if n-1 == m:
#         return True
#     return prostoe(n, m+1)
#
#
# print(prostoe(12))

# int float кол во символов
# def f(*a):
#     return list(map(lambda x: [x, len(str(x))], filter(lambda x: type(x) in [int, float], a)))
# print(f("dfgdgf", ["wetwtet", "rwt"], 35435, 34.1))
#

# сколько натуральных чисел длины а равна сумме цифр б

# сделать через range, рекурсивно
def f(a, b):
    cnt = []
    for i in range(10**(a-1), 10**a-1):
        if sum(int(n) for n in str(i)) == b:
            cnt.append(i)
    return cnt



print(f(2, 6))














# from fnmatch import *
# for x in range(2024,10**10, 2024):
#     if fnmatch(str(x), "10*2024?"):
#         print(x, x//2024)

# from math import ceil
# def f(a, h):
#     if a <= 35:
#         return h%2==0
#     if h == 0:
#         return 0
#     x = [f(a - 2, h - 1), f(a - 4, h - 1), f(ceil(a / 2), h - 1)]
#
#
#     return any(x) if (h-1)%2==0 else all(x)
#
# print("19 --", min([a  for a in range(36,1000) if f(a,2)]))
# print("20 --", [a  for a in range(36,1000) if not(f(a,1)) and f(a,3)])
# print("21 --", [a  for a in range(36,1000) if not(f(a,2)) and f(a,4)])