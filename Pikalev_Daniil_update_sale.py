import sys

def update_sale(price):
    with open ('bakery.csv', 'a', encoding='utf-8') as f:
        f.write(f'{price}\n')


if __name__=='__main__':
    if len(sys.argv) == 2:
        update_sale(sys.argv[1])
    exit(0)
