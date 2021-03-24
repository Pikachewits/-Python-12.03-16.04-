from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(amount):
    joke = []
    for word in range(amount):
        joke.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
    return joke


print(get_jokes(3))