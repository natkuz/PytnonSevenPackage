# ✔ Напишите функцию, которая генерирует псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

import string
from random import randint, sample

NUM_OF_NAMES = randint(3, 10)
vowels = 'aeiouy'

def gen_names():
    names = []
    while len(names) < NUM_OF_NAMES:
        res = sample(string.ascii_lowercase, randint(4, 7))
        if len(set(res) & set(vowels)) > 0:
            names.append(''.join(res).title())
    with open('names.txt', 'a', encoding='utf-8') as f:
        f.writelines('\n'.join(names))

gen_names()
