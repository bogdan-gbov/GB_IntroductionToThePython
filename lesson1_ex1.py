"""
Найдите сумму цифр трехзначного числа n.

Результат сохраните в перменную res.
"""

num = input('Введите трехзначное число: ')
res = 0
if len(num) == 3:
    for i in num:
        res = res + int(i)
    print(res)
else:
    print('Число не трехзначное')