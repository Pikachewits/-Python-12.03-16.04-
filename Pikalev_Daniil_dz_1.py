import re


def email_parse(email):
    my_pattern = re.compile(r'[^@]+@[^@\.]+\.[^@\.]+')
    if my_pattern.fullmatch(email) is None:
        raise ValueError(f'Wrong email: {email}')
    else:
        adress = email.split('@')
        dict = {'username': adress[0], 'domain': adress[1]}
        return dict

print(email_parse('pikalevdo@gmail.com'))
