class Data:

    def __init__(self, full_date):
        self.full_date = str(full_date)

    @classmethod
    def get_date(cls, full_date):
        my_date = list(map(int, full_date.split('-')))
        return my_date

    @staticmethod
    def valid_date(full_date):
        day, month, year = map(int, full_date.split('-'))
        if 1 <= day <= 31 and 1 <= month <= 12 and 0 < year < 2021:
            return f'Всё отработало верно!'
        else:
            return f'Дата неккоректна'


print(Data.get_date('02-07-1995'))
print(Data.valid_date('02-07-1995'))