import math
n=int(input("Напишите количество чисел после запятой:"))
print('{num:.{n}f}'.format(n=n, num=math.pi))
