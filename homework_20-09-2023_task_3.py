'''
Задача № 3:
Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.

'''
import random
import string
import os

'''
Функция из Задания №1 на семинаре
✔ Напишите функцию, которая заполняет файл
(добавляет в конец) случайными парами чисел.
✔ Первое число int, второе - float разделены вертикальной чертой.
✔ Минимальное число - -1000, максимальное - +1000.
✔ Количество строк и имя файла передаются как аргументы функции.

'''
def add_random_pairs_to_file(filename, num_lines):
        with open(filename, "a") as file:
            for _ in range(num_lines):
                int_num = random.randint(-1000, 1000)
                float_num = random.uniform(-1000, 1000)
                line = f"{int_num}|{float_num}\n"
                file.write(line)
        print(f"{num_lines} строчек добавлено в файл {filename}")

'''
Функция мз Задания №2 на семинаре
✔ Напишите функцию, которая генерирует
псевдоимена.
✔ Имя должно начинаться с заглавной буквы,
состоять из 4-7 букв, среди которых
обязательно должны быть гласные.
✔ Полученные имена сохраните в файл.

'''

def generate_pseudonym(filename, directory="."):
    vowels = "AEIOU" ### для избежания ошибок предполагаем, что гласные будут английские
    consonants = "".join(set(string.ascii_uppercase) - set(vowels)) ### получаем множество согласных букв
    name_length = random.randint(4, 7)

    name = random.choice(vowels)

    for _ in range(name_length - 1):
        if _ % 2 == 0:
            name += random.choice(consonants)
        else:
            name += random.choice(vowels)
    
    with open(os.path.join(directory, filename), "a") as file: ### псевдоимя записывается в файл (после имени переход на новую строку), если файла нет, он создается вновь.
            file.write("".join(name))
            file.write('\n')
    
    print(f" Файл с псевдоименем {name} внутри создан в директории: {os.path.join(directory, filename)}")

    return name

'''
Функция из Задания №3 на семинаре
✔ Напишите функцию, которая открывает на чтение созданные
в прошлых задачах файлы с числами и именами.
✔ Перемножьте пары чисел. В новый файл сохраните
имя и произведение:
✔ если результат умножения отрицательный, сохраните имя
записанное строчными буквами и произведение по модулю
✔ если результат умножения положительный, сохраните имя
прописными буквами и произведение округлённое до целого.
✔ В результирующем файле должно быть столько же строк,
сколько в более длинном файле.
✔ При достижении конца более короткого файла,
возвращайтесь в его начало.
'''
def process_files(input_numbers_file1, input_letters_file2, output_file):
    
    with open(input_numbers_file1, 'r') as file1: 
        numbers = file1.readlines()
                
    with open(input_letters_file2, 'r') as file2:    
        letters = file2.readlines()

        # Определение содержание какого файла больше
        max_length = max(len(numbers), len(letters))

        with open(output_file, 'a') as output:
            for i in range(max_length):
                # Выбор чисел и имен из содержания файлов
                number1, number2 = numbers[i % len(numbers)].strip('\n').split('|')
                name = letters[i % len(letters)].strip('\n')

                # Конвертация строк в числа
                number1 = int(number1)
                number2 = float(number2)

                # Обределение произведения чисел
                product = number1 * number2
                if product < 0:
                    name = name.lower()
                    product = abs(product)
                else:
                    name = name.upper()
                    product = round(product)

                # Запись имен и результатов умножения в файл
                output.write(f'{name} | {product}\n')

        print(f'Результаты сохранены в файл {output_file}')

'''
Функция из Задачи № 2 домашнего задания: 
Напишите функцию группового переименования файлов. Она должна:
✔ принимать параметр желаемое конечное имя файлов.
При переименовании в конце имени добавляется порядковый номер.
✔ принимать параметр количество цифр в порядковом номере.
✔ принимать параметр расширение исходного файла.
Переименование должно работать только для этих файлов внутри каталога.
✔ принимать параметр расширение конечного файла.
✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона
[3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

'''
def rename_files(final_names, num_digits, source_ext, end_ext, name_range, directory="."):
    # Получение списка файлов в директории (по умолчанию текущая директория)
    files = [f for f in os.listdir(directory) if f.endswith(source_ext)]

    # сортировка имен файлов
    files.sort()

    # Создание счетчика файлов
    file_counter = 1

    # Проход по всем файлам и их переименование
    for filename in files:
        # Выделение диапазона из сохраняемого оригинального имени 
        start, end = name_range
        original_name_part = filename[start - 1:end]

        # Создание нового имени файла
        new_filename = f"{final_names}{original_name_part}_{str(file_counter).zfill(num_digits)}.{end_ext}"

        # Создание полного имени файла (по умолчанию текущая директория)
        current_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_filename)

        # Переименование файла
        os.rename(current_path, new_path)

        # Увеличение порядкового номера файла
        file_counter += 1

if __name__ == "__main__":
    # Проверка работы функции из задачи №1 семинара:
    file_name = "file_seminar_task_1.txt"   
    num_lines_to_add = 10       # указываем сколько строк нужно добавить в файл
    add_random_pairs_to_file(file_name, num_lines_to_add)
    print('Функция из задачи №1 семинара закончила работать.')

    # Проверка работы функции из задачи №2 семинара:
    generate_pseudonym(filename= "file_seminar_task_2.txt")
    print('Функция из задачи №2 семинара закончила работать.')

    # Проверка работы функции из задачи №3 семинара:
    input_file1 = 'file_seminar_task_1.txt'  # имя файла с числами
    input_file2 = 'file_seminar_task_2.txt'  # имя файла с именами
    output_file = 'file_seminar_task_3.txt'  # имя выходного файла
    process_files(input_file1, input_file2, output_file)
    print('Функция из задачи №3 семинара закончила работать.')

    # Проверка работы функции из задачи №2 домашнего задания
    final_names = "new_file_name"     # Передача желаемого конечного имени файлов 
    num_digits = 3                    # Передача количества цифр в порядковом номере
    source_ext = ".txt"               # Передача расширения исходного файла
    end_ext = "pdf"                   # Передача расширения конечного файла
    name_range = (3, 6)               # Передача диапазона сохраняемого оригинального имени
    
    rename_files(final_names, num_digits, source_ext, end_ext, name_range)
    print('Функция из задачи №2 домашнего задания закончила работать.')
