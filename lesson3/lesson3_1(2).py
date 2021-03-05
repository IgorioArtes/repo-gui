def num_translate(word):
    word_new = word.title()
    trans = {"one": "один",
             "two": "два",
             "three": "три",
             "four": "четыре",
             "five": "пять",
             "six": "шесть",
             "seven": "семь",
             "eight": "восемь",
             "nine": "девять",
             "ten": "десять"}
    if word.istitle():
        for i in trans:
            if word_new == trans[i].title():
                return f'{word_new} = {i.title()}'
            elif word_new == i.title():
                return f'{word_new} = {trans[word].title()}'
        return f' none '
    else:
        for i in trans:
            if word == trans[i]:
                return f'{word} = {i}'
            elif word == i:
                return f'{word} = {trans[word]}'
        return f' none '


print(num_translate(input("Введите числительное от 1-10: ")))
