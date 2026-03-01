# 1

# print(4, 12, 15, 43)

# print(123, 236, 13, 17)

# print(10)
# print(20)
# print(30)

# print('% .5f '% 45.4894654)

# print("%.3f"% (7/13))


# a = int(input(""))
# b = int(input(""))
# print(a, "+", b,"=", a+b)
# print(a, "-", b,"=", a-b)
# print(a, "*", b,"=", a*b)
# print(a, "/", b,"=", a/b)

# a = float(input(""))
# b = float(input(""))
# a, b = b, a
# print(a, b)

# a = int(input(""))
# b = int(input(""))
# c = int(input(""))
# print(c // (a+b), "=" "")
# print(c % (a+b), "=" "")

# a = int(input(""))
# b = a // 10
# c = a % 10
# print(b + c, "=" "")

# a = int(input(""))
# b = a // 10
# c = a % 10
# print(c*10 + b)

# a = int(input(""))
# b = a//100
# c = a%100
# d = a%10
# print(b, c, d)

# a = float(input(""))
# b = a//1000
# print(b)

# a = int(input(""))
# b = int(input(""))
# c = b - a
# print(c)

# a, b = map(float, input(""). split())
# print((a+b) / 2)

# 3

# a, b = map(float, input(""). split())
# if a > b:
#     print(a)
# else:
#     print(b)

# a = int(input(""))
# if a % 2 == 0:
#     print(a+2)
# else:
#     print(a+1)

# a, b, c = map(float, input(""). split())
# D = a
# if b < D:
#     D = b
# if c < D:
#     D = c
# print(D)

# a, b, c, d = map(float, input(""). split())
# k = 0
# if a % 2 == 0:
#     k += 1
# if b % 2 == 0:
#     k += 1
# if c % 2 == 0:
#     k += 1
# if d % 2 == 0:
#     k += 1
# print(k)

# a, b, c, d, e, f = map(float, input(""). split())
# k = 0
# if a > 0:
#     k += 1
# if b > 0:
#     k += 1
# if c > 0:
#     k += 1
# if d > 0:
#     k += 1
# if e > 0:
#     k += 1
# if f > 0:
#     k += 1
# print(k)

# a, b, c, d, e, f = map(float, input(""). split())
# k = 0
# if a > 0:
#     k += a
# if b > 0:
#     k += b
# if c > 0:
#     k += c
# if d > 0:
#     k += d
# if e > 0:
#     k += e
# if f > 0:
#     k += f
# print(k)

# x, y = map(float, input(""). split())
# if x > 0 and y > 0:
#     print("I четверть")
# if x < 0 and y > 0:
#     print("I четверть")
# if x < 0 and y < 0:
#     print("I четверть")
# if x > 0 and y < 0:
#     print("I четверть")

# x1, y1 = map(float, input(""). split())
# x2, y2 = map(float, input(""). split())
# x3, y3 = map(float, input(""). split())
# if x2 == x3:
#     x4 = x1
# if x3 == x1:
#     x4 = x2
# if x2 == x1:
#     x4 = x3
# if y2 == y3:
#     y4 = y1
# if y2 == y3:
#     y4 = y1
# if y2 == y3:
#     y4 = y1
# print(x4, y4)

# a, b, c = map(float, input(""). split())
# if a < b + c and b < a + c and c < a+ b:
#     print("Yes")
# else:
#     print("No")

# 4

# n = int(input('Введите число n: '))
# for i in range(1, n + 1):
#     print(i ** 2)

# print('Программа вывода чисел в порядке убывания')
# a, b = map(int, input('Введите два числа -> '). split())
# for i in range(b, a - 1, -1):
#     print(i, end = ' ')


# print ("ярды", "метры")
# for i in range(1, 11):
#     print(i, i * 0.9144, sep = "   ")

# print("Программа вывода таблицы умножения")
# n = int(input("Введите число: "))
# for i in range(1, 10):
#     print(i, "x", n, "=", i * n)

# a, b = map(int, input(). split())
# for i in range(a, b+1):
#     if i % 2 ==0:
#         print(i, end = "  ")

# for i in range (10, 100):
#     if i % 10 == 2 or i % 10 == 6:
#         print (i)

# a = int(input())
# for i in range (10, 100):
#     if (i //10) + (i % 10) == a:
#         print (i, end = "  ")

# a, b, c = map(int, input(). split())
# d = 0
# for i in range(a, b+1):
#     if i % c ==0:
#         d +=1
#         print (i)
# print (d)

# s = 0
# for i in range (101, 1000, 2):
#     s += i
# print (s)

# 5

# a = int(input())
# c = 1
# while c <= a:
#     print(c, end = "")
#     c += 1

# a, b = map(int, input(). split())
# c = a
# while c <= b:
#     if c % 2 == 0:
#         print (c, end =" ")
#     c += 1

# a = int(input())
# count = 0
# while a != 0:
#     b = a % 10
#     count += b
#     a //= 10
# print (count)

# a = int(input())
# b = 0
# while a != 0:
#     b += 1
#     a //=10
# print(b)

# a = int(input())
# b = 1
# while a != 0:
#     c =  a % 10
#     b *=c
#     a //= 10
# print(b)

# a = int(input())
# while a != 0:
#     b = a % 10
#     print (b, end = " ")
#     a = a // 10

# a = int(input())
# for i in range(a-1, -1, -1):
#     b = a % 10
#     a //= 10
#     print(i)

# a = int(input())
# b = 0
# while a != 0:
#     c = a % 10
#     if c ==5:
#         print("да")
#         b = 1
#         break
#     a //= 10
# if a != 1:
#     print("no")


# a = 1
# b = int(input())
# while b != 0:
#     a *= b
#     b = int(input())
# print('Произведение чисел равно', a)


# b = int(input())
# a = 1
# while (a ** 2) <= b:
#     print(a ** 2, end =" ")
#     a += 1