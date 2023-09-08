# ✔ Напишите функцию группового переименования файлов. Она должна:
# ✔ принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# ✔ принимать параметр количество цифр в порядковом номере.
# ✔ принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# ✔ принимать параметр расширение конечного файла.
# ✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона
# [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
# желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

import os

def rename_files(list_files: list, files_path: str = 'images/', num_digits: int = 5, extention: str = 'png',
                 range_letters: list = [2, 5], new_name: str = 'NAME'):
    list_for_ext = []
    for obj in list_files:
        list_for_ext.append(obj.split('.'))
    print(list_for_ext)

    count = 0
    for i in list_for_ext:
        part_one = i[0][range_letters[0]:range_letters[1]]
        count += 1
        zeroes = num_digits - len(str(count))
        name = part_one+new_name+('0' * zeroes)+str(count)+'.'+extention
        if os.path.exists(files_path):
            os.rename(f'{files_path}{i[0]}.{i[1]}', f'{files_path}{name}')
        else:
            print("Такой папки не существует")


rename_files(os.listdir('images'))