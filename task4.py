# 4. * (вместо задачи 3) Написать функцию thesaurus_adv(),
# принимающую в качестве аргументов строки в формате «Имя Фамилия» и возвращающую словарь,
# в котором ключи — первые буквы фамилий, а значения — словари,
# реализованные по схеме предыдущего задания и содержащие записи,
# в которых фамилия начинается с соответствующей буквы.
# Например:
# >>> >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# {
#     "А": {
#         "П": "Петр Алексеев"
#     },
#     "С": {
#         "И": ["Иван Сергеев", "Инна Серова"],
#         "А": ["Анна Савельева"]
#     }
# }
# Сможете ли вы вернуть отсортированный по ключам словарь?
list_of_employees = {}


def thesaurus_adv(name, surname):
    """Составляет словарь по фамилиям, затем по именам"""
    # Объединяем в полное имя
    full_name = f'{name} {surname}'
    # Берем первую букву имени
    first_letter_name = name[0]
    first_letter_name.upper()
    # Берем вторую букву имени
    first_letter_surname = surname[0]
    first_letter_surname.upper()
    # Есть ли первая буквы фамилии уже в словаре
    if first_letter_surname in list_of_employees:
        # Если есть, то есть ли первая буква имени уже в словаре
        if first_letter_name in list_of_employees[first_letter_surname]:
            # Если есть и то и то, добавлем новое полное ФИ
            # name_dict - просто скоращенный путь(не спускаемся вниз на два словаря, а просто получаем букву
            # уже от существующего словаря. Например: словарь М(name_dict), получаем из него ключ -
            # Е(name_dict[first_letter_name])
            name_dict = list_of_employees[first_letter_surname]
            name_dict[first_letter_name].append(full_name)
        else:
            # Если есть первая буква Ф но нет буквы И
            name_dict = list_of_employees[first_letter_surname]
            # Создаем пустой список для этой буквы имени
            name_dict[first_letter_name] = []
            # Добавляем в пустой список ФИ
            name_dict[first_letter_name].append(full_name)
    else:
        # Если нету ни первой буквы фамил. ни первой буквы имени то создаем пустой словарь, называя его перв. буква фам.
        list_of_employees[first_letter_surname] = {}
        # name_dict - просто скоращенный путь(не спускаемся вниз на два словаря, а просто получаем букву
        # уже от существующего словаря. Например: словарь М(name_dict), получаем из него ключ -
        # Е(name_dict[first_letter_name])
        name_dict = list_of_employees[first_letter_surname]
        # Создаем пустой список для перой буквы имени для этой первой буквы фамилии
        name_dict[first_letter_name] = []
        # Добавляем в пустой список полное ФИ
        name_dict[first_letter_name].append(full_name)
    # Сортируем словарь
    list_of_employees_sorted = {key: val for key, val in sorted(list_of_employees.items())}
    # Возвращаем отсортированный словарь
    print(list_of_employees_sorted)


while True:
    # Вводим имя и фамилию нового сотродника
    first_name, last_name = map(str, input('Введите имя и фамилию сотрудников: ').split())
    # Вызываем функцию сортировки и добавления нового человека в словарь
    thesaurus_adv(first_name, last_name)
