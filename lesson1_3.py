# Реализовать склонение слова «процент» для чисел до 20. Например, задаем число 5 — получаем «5 процентов»,
# задаем число 2 — получаем «2 процента». Вывести все склонения для проверки.
number = input('enter your number')
if int(number) == 1:
    print(f'{number} процент')
if int(number) == 2 or int(number) == 3 or int(number) == 4:
    print(f'{number} процента')
if 5 <= int(number) <= 20:
    print(f'{number} процентов')
