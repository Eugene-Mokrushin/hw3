# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имен, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# Например:
# >>> >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"], "П": ["Петр"]
# }


# Создаем словарь сотрудников
list_of_employees = {}


def thesaurus(names):
    """Возвращает отсортированный словарь сотрудников по первой букве имени"""
    # Перебираем переданный список имен
    for name in names:
        # Берем заглавную первую букву имени
        first_letter_name = name[0].upper()
        # Есть ли уже первая буква имени как ключ в словаре
        if first_letter_name in list_of_employees:
            # Если да, добавляем ее в список по ключу first_letter_name
            list_of_employees[first_letter_name].append(name)
        else:
            # Если нет, создаем ключ с этой буквой и привязываем к нему пустой словарь
            list_of_employees[first_letter_name] = []
            # Добавляем в этот пустой словарь новое имя
            list_of_employees[first_letter_name].append(name)
    # Создаем новый словарь для сортировке по ключам (иначе никак)
    sorted_list_of_employees = {}
    # Получаем отсортированный список ключей
    sorted_keys = sorted(list_of_employees, key=list_of_employees.get)
    # Из старого списка присваиваем по ключу значения в новый список
    for key in sorted_keys:
        sorted_list_of_employees[key] = list_of_employees[key]
    print(sorted_list_of_employees)


while True:
    # Вводить можно как одно новое имя, так и несколько новых имен сразу, через пробел
    first_name = list(map(str, input('Введите имена сотрудников: ').split()))
    thesaurus(first_name)
