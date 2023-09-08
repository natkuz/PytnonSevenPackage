# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

import os
import shutil

def sort_files(dir_list):
    list_for_ext = []
    for obj in dir_list:
        if os.path.isfile(obj):
            list_for_ext.append(obj.split('.'))

    list_text_files = ['txt', 'doc', 'xls', 'json', 'csv']
    list_img_files = ['png', 'jepg', 'jpg', 'bmp']
    list_video_files = ['vawe', 'mkv', 'mp4']
    list_audio_files = ['mp3', 'mpg']
    for i in list_for_ext:
        if i[1] in list_text_files:
            if not os.path.isdir('text'):
                os.mkdir('text')
            shutil.move(f'{i[0]}.{i[1]}', 'text')
        elif i[1] in list_video_files:
            if not os.path.isdir('video'):
                os.mkdir('video')
            shutil.move(f'{i[0]}.{i[1]}', 'video')
        elif i[1] in list_img_files:
            if not os.path.isdir('images'):
                os.mkdir('images')
            shutil.move(f'{i[0]}.{i[1]}', 'images')
        elif i[1] in list_audio_files:
            if not os.path.isdir('audio'):
                os.mkdir('audio')
            shutil.move(f'{i[0]}.{i[1]}', 'audio')

sort_files(os.listdir())


