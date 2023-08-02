"""
При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значение `n`

При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения `n` для проверки
"""
#n == countPetya + countSerezha + countKatya
#n == countPetya + countPetya + 2*(countPetya + countPetya)
#n == 2countPetya + 4countPetya
#countPetya = n/6

n = 6

# Введите ваше решение ниже
countPetya = round(n/6)
countSerezha = round(n/6)
countKatya = round(2*(countPetya+countSerezha))

count = (countPetya, countKatya, countSerezha)

print(count)
