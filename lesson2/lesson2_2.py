my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+1', 'градусов']
indexlist = []
result_list = ''
for i, v in enumerate(my_list):
    if v.isdigit():
        if (int(v) // 10) == 0:
            my_list[i] = str(0) + str(v)
        indexlist.append(i)
    elif v[1:].isdigit():
        if (int(v) // 10) == 0 or (int(v) // 10) == -1:
            my_list[i] = str(v[:1]) + str(0) + str(v[1:])
        indexlist.append(i)
print(indexlist)
for i, v in enumerate(indexlist):
    my_list.insert(i * 2 + int(v) + 1, '"')
    my_list.insert(i * 2 + int(v), '"')
print(my_list)
t = 1
for i, v in enumerate(my_list):
    if v == '"':
        if t==1:
            result_list += str(v)
            t = 0
        else:
            result_list += str(v)+' '
    elif v.isdigit() or v[1:].isdigit():
        result_list += str(v)
    else:
        result_list += str(v) + ' '
        t=1
print(result_list)
