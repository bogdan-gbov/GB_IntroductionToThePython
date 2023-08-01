"""
Найдите сумму цифр трехзначного числа n.

Результат сохраните в перменную res.
"""

num = input('Введите трехзначное число: ')
result = 0
if len(num) == 3:
    for i in num:
        result = result + int(i)
    print(result)
else:
    print('Число не трехзначное')