def f(a,b):
    if b == 0:
        return 1
    return a * f(a, b-1)

expo = f((int(input("Введите число: "))), (int(input("Введите степень: "))))

print("Итого: ", expo)