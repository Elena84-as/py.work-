import os
import time
import os.path
print('Текущая директория :', os.getcwd())

directory = '.'

for root,dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(file)
        filetime = os.path.getmtime
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime())
        filesize =os.path.getsize(b'test.txt')
        parent_dir = os.path.dirname(file)
print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time},'
      f' Родительская директория: {parent_dir}')

