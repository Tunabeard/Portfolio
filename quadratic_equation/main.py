import math

def equation_review(a, b, c):    # Не необходимо (вся функция)
    mod1, mod2 = " + ", " + "
    if b < 0:
        mod1 = " – "
    if c < 0:
        mod2 = " – "
    numbers = [a, b, c]
    for num in numbers:
        if num == 1 and numbers.index(num) != 2:
            numbers[numbers.index(num)] = ""
        elif num%1 == 0:
            numbers[numbers.index(num)] = str(abs(int(num)))
    print("Ваше уравнение: " + numbers[0] + "x\u00b2" + mod1 + numbers[1] + "x" + mod2 + numbers[2] + " = 0")

def quadratic_equation(a, b, c):
    if a == 0 or b == 0:
        print("Это не квадратное уравнение!")
        return []
    else:
        equation_review(a, b, c)
    results = []
    discriminant = (b**2)-(4*a*c)
    if discriminant%1 == 0:
        discriminant = int(discriminant)
    print("Дискриминант: " + str(discriminant))     # Не необходимо
    if discriminant < 0:
        print("Корней нет.")
        return []
    elif discriminant == 0:
        results.append(round((-b/(2*a)), 3))
    else:
        results.append(round(((-b+math.sqrt(discriminant))/(2*a)), 3))
        results.append(round(((-b-math.sqrt(discriminant))/(2*a)), 3))
    print("Корни:")     # Не необходимо
    for num in results:     # Не необходимо (весь блок)
        if num%1 == 0:
            print(str(int(num)))
        else:
            print(str(num))
    return results

print("Паттерн квадратного уравнения: ax\u00b2 + bx + c = 0")
while True:
    try:
        num1 = float(input("Введите число а: "))
        num2 = float(input("Введите число b: "))
        num3 = float(input("Введите число c: "))
        break
    except ValueError:
        print("Вы ввели некорректное значение. Попробуйте ещё раз.")
print()     # Не необходимо
quadratic_equation(num1, num2, num3)