def get_jokes(n):
    from random import randrange

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    c=[]

    for i in range(1, n+1):
        b = nouns[randrange(0, len(nouns))] + ' ' + adverbs[randrange(0, len(adverbs))] + ' ' + adjectives[
            randrange(0, len(adjectives))] + ' '
        c.append(b)

    return c


print(get_jokes(10))
