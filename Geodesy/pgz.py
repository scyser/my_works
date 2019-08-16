import math

X1 = float(input("Введите X1: "))
Y1 = float(input("Введите Y1: "))

print("Введение дирекционного угла")
grad = float(input("Введите градусы: "))
minut = float(input("Введите минуты: "))
sec = float(input("Введите секунды: "))
print(" ")
d = float(input("Введите расстояние до точки 2: "))

alpha = math.radians(grad+minut/60+sec/3600)

X2 = X1 + d*math.cos(alpha)
Y2 = Y1 + d*math.sin(alpha)

print(" ")
print("X2 = : " + str(X2))
print("Y2 = : " + str(Y2))
