def thesaurus(*args):
    dict_names = {}
    for item in args:
        first_letter = item[0]
        if not dict_names.get(first_letter):
            dict_names[first_letter] = [item]
        else:
            dict_names[first_letter].append(item)

    return dict_names


result = thesaurus('Даня', 'Коля', 'Иван', 'Даша', 'Люба', 'Наташа', 'Николай', 'Максим')
print(result)