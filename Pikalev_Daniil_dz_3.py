tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Артем', 'Кирилл']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def generator (student_name, klass_name):
    excess = len(student_name) - len(klass_name)
    if excess > 0:
        klass_name.extend([None for i in range(excess)])
    for t, k in zip(student_name, klass_name):
        yield t, k


some_generator = generator(tutors, klasses)
print(list(some_generator))
