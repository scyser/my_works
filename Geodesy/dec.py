def dec(deg, min, sec=0):
    """Перевод г/м/с в десятичную форму"""
    ungle = deg + min/60 + sec/3600
    return ungle
