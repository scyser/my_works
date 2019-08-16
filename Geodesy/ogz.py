import math

X1 = float(input("Введите X1: "))
Y1 = float(input("Введите Y1: "))
X2 = float(input("Введите X2: "))
Y2 = float(input("Введите Y2: "))

dX = X2 - X1
dY = Y2 - Y1

D = math.sqrt(dX**2+dY**2)

if dX>0:
    if dY>0:
        alpha = math.degrees(math.atan(math.fabs(dY/dX)))
    else:
        alpha = math.degrees(math.atan(math.fabs(dX/dY))) + 270
else:
    if dY>0:
        alpha = math.degrees(math.atan(math.fabs(dX/dY))) + 90
    else:
        alpha = math.degrees(math.atan(math.fabs(dY/dX))) + 180

grad = math.trunc(alpha)
minut = math.trunc((alpha - grad)*60)
sec = (((alpha-grad)*60)%1)*60
        
def toFixed(sec, digits=0):
    return f"{sec:.{digits}f}"

print("Расстояние равно: " + str(D))
print("Дирекционный угол равен: " + str(grad) + " град " + str(minut) + " мин " + str(toFixed(sec, 2)) + " сек" )
