# ✔ Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк, сколько в более длинном файле.
# ✔ При достижении конца более короткого файла, возвращайтесь в его начало.

def names_and_product(file_names, file_nums):
    names, numbers = None, None
    with (
        open(file_names, 'r', encoding='utf-8') as names,
        open(file_nums, 'r', encoding='utf-8') as nums
    ):
        numbers = nums.readlines()
        names = names.readlines()
    numbers = list(map(lambda x: int(x.strip().split(' | ')[0]) * float(x.strip().split(' | ')[1]), numbers))
    names = list(map(lambda x: x.strip(), names))
    list_to_write = list(zip(names, numbers))
    with open('result.txt', 'a', encoding='utf-8') as res:
        for st in list_to_write:
            if st[1] > 0:
                res.write(f'{st[0].upper()} -> {round(st[1])} \n')
            else:
                res.write(f'{st[0].lower()} -> {abs(st[1])} \n')


names_and_product('names.txt', 'seminar_07_01.txt')