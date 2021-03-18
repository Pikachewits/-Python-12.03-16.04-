words = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

new_words = []
count = 0

for word in words:
    if word.isdigit() or (word[0] in ('+', '-') and word[1:].isdigit()):
        if word[0] in ('+', '-'):
            word = f'"{word[0]}{int(word[1:]):02}"'
            new_words.insert(count, word)
        else:
            word = f'"{int(word):02}"'
            new_words.insert(count, word)
    else:
        new_words.insert(count, word)
    count += 1

result = ' '.join(new_words)
print(result)
