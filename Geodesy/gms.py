def gms(ungle):
    """Перевод и вывод десятичных градусов в г/м/с"""
    deg = int(ungle - (ungle%1))
    min = int((ungle-deg) * 60 - ((ungle-deg)*60)%1)
    sec = round((((ungle-deg)*60)%1) * 60, 2)
    return deg, min, sec
