num = input("Введите число")
y = 0
mo = 0
d = 0
m = 0
s = 0
if int(num) // 31536000 > 0:
    y = int(num) // 31536000
    num = int(num) - y * 31536000
    print(f'{y} years')
if int(num) // 2628000 > 0:
    mo = int(num) // 2628000
    num = int(num) - mo * 2628000
    print(f'{mo} months')
if int(num) // (3600 * 24) > 0:
    d = int(num) // 86400
    num = int(num) - d * 86400
    print(f'{d} days')

if int(num) // 3600 > 0:
    h = int(num) // 3600
    print(f'{h} hours')
    num = int(num) - h * 3600
if int(num) // 60 > 0:
    m = int(num) // 60
    print(f'{m} minutes')
    num = int(num) - m * 60
    s = int(num)
    print(f'{s} seconds')
else:
    m = 0
    s = int(num)
    print(f'{m} minutes')
    print(f'{s} seconds')
print(f'{y} years {mo} months {d} days {h} hours {m} minutes {s} seconds')
