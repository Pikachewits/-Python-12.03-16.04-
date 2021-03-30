import sys
from Lesson_4.my_utils.currency_rates import currency_rates

if __name__ == "__main__":
    print(currency_rates('aud'))

    programm = sys.argv[0]
    currency_result = currency_rates(programm)
    print(f'{currency_result[0]}')
    exit(0)