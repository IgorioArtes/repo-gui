def thesaurus(*names):
    out = {}
    first_letter = []
    for n in names:
        first_letter.append(n[0])
    name = []
    print(first_letter)
    first_letter = set(first_letter)
    print(first_letter)
    for fn in first_letter:
        for n in names:
            if fn == n[0]:
                name.append(n)
        out[fn] = name.copy()
        name.clear()
    return out


# print(type(set(first_letter)))

print(thesaurus("Иван", "Мария", "Петр", "Илья", "Игорь", "Василий"))
