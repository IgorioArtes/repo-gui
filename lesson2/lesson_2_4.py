my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for i in range(0, len(my_list)):
    s = my_list[i].split(' ')[len(my_list[i].split(' ')) - 1].title()
    print(f'Hello, {s}!')
