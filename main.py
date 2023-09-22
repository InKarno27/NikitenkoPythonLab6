"""
Лабораторная 6 Вариант 9
Написать функцию, которая принимает путь к файлу с расширением .txt, который содержит данные для заполнения
таблицы, и по указанным в файле данным создает таблицу или таблицы и заполняет их данными.
"""

def read_tables_from_file(file_path):
    tables = []
    with open(file_path, 'r') as f:
        lines = f.readlines()
        current_table = []
        for line in lines:
            if line.strip() == '':
                # Пустая строка - конец текущей таблицы, добавляем ее в список таблиц
                tables.append(current_table)
                current_table = []
            else:
                # Непустая строка - добавляем ее в текущую таблицу
                row = line.strip().split(',')
                current_table.append(row)
        # Добавляем последнюю таблицу
        tables.append(current_table)
    return tables

file_path = 'example.txt'
table = read_tables_from_file(file_path)
for row in table:
    print(row)