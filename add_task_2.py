def digit_root(num):
    if num < 0:
        return "Число должно быть неотрицательным"

    while pow(10,7) > num >= 10:
        summa = 0
        while num > 0:
            summa += num % 10
            num //= 10
        num = summa
    return num




print(digit_root(12345678909))
print(digit_root(-97569))  
print(digit_root(889987))  