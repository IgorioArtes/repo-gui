def thesaurus(*names):
    out = {}
    lastout = {}
    first_letter = []
    second_name = []
    for n in names:
        second_name.append(n[n.find(' ') + 1])
    name = []
    second_name = set(second_name)
    first_letter = set(first_letter)
    for sn in second_name:
        for n in names:
            h = (n[n.find(' ') + 1])
            if sn == h:
                name.append(n)
        for i in name:
            first_letter.add(i[0])
        first_letter.clear()
        lastout[sn] = name.copy()
        name.clear()
    name.clear()
    out.clear()
    for i in lastout:
        for n in lastout[i]:
            first_letter.add(n[0])
        for fn in first_letter:
            for n in lastout[i]:
                if fn == n[0]:
                    name.append(n)
            out[fn] = name.copy()
            name.clear()
        lastout[i] = out.copy()
        out.clear()
        first_letter.clear()

    return lastout


print(thesaurus("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
