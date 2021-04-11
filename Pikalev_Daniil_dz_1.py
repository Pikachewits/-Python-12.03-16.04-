import os

folders = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}

for key, val in folders.items():
    if not os.path.isdir(key):
        os.mkdir(key)
    for some_folder in val:
        dir_path = os.path.join(key, some_folder)
        if not os.path.isdir(dir_path):
            os.mkdir(dir_path)

