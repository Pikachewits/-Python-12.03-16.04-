import json

result_dict = {}

with open('task_3_people.txt', 'r', encoding='utf-8') as people, open('task_3_hobbies.txt', 'r', encoding='utf-8') as hobbies:
    key = people.readline().strip().replace(',', ' ')
    val = hobbies.readline().strip().replace(',', ', ')

    while key:
        result_dict.update({key:val})
        key = people.readline().strip().replace(',', ' ')
        val = hobbies.readline().strip().replace(',', ', ')

print(result_dict)

with open ('task_3_results', 'w+', encoding='utf-8') as f:
    json.dump(result_dict, f)