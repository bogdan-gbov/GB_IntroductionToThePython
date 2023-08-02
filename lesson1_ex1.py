"""
Найдите сумму цифр трехзначного числа n.

Результат сохраните в перменную res.


num = input('Введите трехзначное число: ')
res = 0
if len(num) == 3:
    for i in num:
        res = res + int(i)
    print(res)
else:
    print('Число не трехзначное')

Код выше не проходит через автотестер
"""

n = str(234)
n = str(n)
res = int(n[0]) + int(n[1]) + int(n[2])
print(res)