import random
import math

rub = 0
kop = 0
count_price = 20
my_price = [38.0]
for i in range(1, count_price):
    my_price.append(round(random.triangular(1, 100), 2))
print(my_price)
v = ''
for i in my_price:
    rub = int(i // 1)
    if rub >= 10:
        kop = int((round(i * 100)) % 100)
    else:
        kop = int(round(i * 100) % 100)
    if kop < 10 and kop != 0:
        kop = str('0' + str(kop))
    elif kop == 0:
        kop = str('00')
    v += str(rub) + ' руб ' + str(kop) + ' коп, '
print(f'задание A: ')
print(v)
print('#'*100)
print(f'залание B: ')
print(id(my_price))
my_price.sort()
print(my_price)
print(id(my_price))
print('#'*100)
print(f'залание C: ')
my_price_sorted = []
my_price_sorted = sorted(my_price)
my_price_sorted.reverse()
print(my_price_sorted)
print(id(my_price_sorted))
print('#'*100)
print(f'залание D: ')
print(my_price[-5:])