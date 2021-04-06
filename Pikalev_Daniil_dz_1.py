import requests

response = requests.get('https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs').text

with open('nginx_logx', 'w', encoding='utf-8') as f:
    f.write(response)

with open('nginx_logx', 'r', encoding='utf-8') as file_1:
    data_list = []
    for line in file_1:
        element = line.split()
        data_list.append((element[0], element[5].strip('"'), element[6]))

    print('Первые 10 кортежей: ')
    print(*data_list[:10], sep='\n')
