import os

some_data = r'C:\Users\User\PycharmProjects\pythonProject\Python_basic\some_data'

very_high_number = 100000
high_number = 10000
middle_number = 1000
low_number = 100

small_files = [item for item in os.listdir(some_data)
               if os.stat(os.path.join(some_data, item)).st_size < low_number]

middle_files = [item for item in os.listdir(some_data)
               if middle_number > os.stat(os.path.join(some_data, item)).st_size > low_number]

big_files = [item for item in os.listdir(some_data)
               if high_number > os.stat(os.path.join(some_data, item)).st_size > middle_number]

very_big_files = [item for item in os.listdir(some_data)
               if very_high_number > os.stat(os.path.join(some_data, item)).st_size > high_number]

result_dict = {low_number:len(small_files),
               middle_number:len(middle_files),
               high_number:len(big_files),
               very_high_number:len(very_big_files)
               }
print(result_dict)
