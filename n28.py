def f(a, b):
    if a < 0 | b < 0:
        return ' Нельзя вводить отрицательные числа '
    if a == 0:
        return b
    return f(a-1,b) + 1

new_sum = f((int(input("Введите первое число: "))), (int(input("Введите второе число: "))))

print("Сумма: ", new_sum)