# one if the first projects in my life

import math

while True:
    print("Теорема косинусов!")
    print("Выберите недостающий элемент:")
    print("Введите 'ugol', если ищите угол")
    print("Введите 'main', если ищите сторону напротив угла")
    print("Введите 'submain', если ищите сторону не напротив угла")
    print("Введите 'vihod', если хотите закрыть программу")
    user_input = input(": ")

    if user_input == "vihod":
        break 
    elif user_input == "ugol":
        a = float(input("Введите длину стороны напротив угла: "))
        b = float(input("Введите первую сторону не напротив угла: "))
        c = float(input("Введите вторую сторону не напротив угла: "))
        calpha = (b**2 + c**2 - a**2)/(2*b*c)
        alpha = math.acos(calpha)
        alpha = math.degrees(alpha)
        grad = math.trunc(alpha)
        minut = math.trunc((alpha - grad)*60)
        sec = (((alpha-grad)*60)%1)*60

        def toFixed(sec, digits=0):
            return f"{sec:.{digits}f}"

        print(" ")
        print("Угол равен: " + str(grad) + " град " + str(minut) + " мин " + str(toFixed(sec, 2)) + " сек" )
        print(" ")
        
    elif user_input == "main":
        print("Укажите данные противолежащего угла")
        grad = float(input("Введите градусы: "))
        minut = float(input("Введите минуты: "))
        sec = float(input("Введите секунды: "))
        b = float(input("Введите первую сторону не напротив угла: "))
        c = float(input("Введите вторую сторону не напротив угла: "))

        alpha = math.radians(grad+minut/60 + sec/3600)

        a = math.sqrt(b**2 + c**2 - 2*b*c*math.cos(alpha))

        print(" ")
        print("Сторона равна: " + str(a))
        print(" ")
        
    elif user_input == "submain":
        print("Укажите данные известного угла")
        grad = float(input("Введите градусы: "))
        minut = float(input("Введите минуты: "))
        sec = float(input("Введите секунды: "))
        a = float(input("Введите сторону напротив угла: "))
        c = float(input("Введите сторону не напротив угла: "))

        alpha = math.radians(grad + minut/60 + sec/3600)

        sgamma = math.sin(alpha) * c / a
        beta = math.pi - math.asin(sgamma) - alpha
        b = math.sin(beta) * a / math.sin(alpha)

        print(" ")    
        print("Сторона равна: " + str(b))
        print(" ")    
        
    else:
        print("Unknown input")


