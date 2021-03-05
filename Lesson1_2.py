l = []
for i in range(1, 1000, 2):
    l.append(i ** 3)
allsums = 0
for i in l:
    t = i
    sums = 0
    while t / 10 > 0:
        d = t % 10
        t = t // 10
        sums += d
    if sums % 7 == 0:
        allsums += i
print(allsums)
#################################################################
allsums = 0
for i in l:
    t = i + 17
    sums = 0
    while t / 10 > 0:
        d = t % 10
        t = t // 10
        sums += d
    if sums % 7 == 0:
        allsums += i + 17
print(allsums)
##################################################################
