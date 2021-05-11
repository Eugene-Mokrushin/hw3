# 2. * (вместо задачи 1)
# Доработать предыдущую функцию num_translate_adv():
# реализовать корректную работу с числительными, начинающимися с заглавной буквы. Например:
# >>> >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"


# Словарь числительных англ на рус
eng_to_rus_dict = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate_adv(eng_word):
    """Возвращает числительное от 1 до 10 на русском"""

    return eng_to_rus_dict.get(eng_word, 'Такого слова в словаре не найдено')


while True:
    # Вводим числительное (прописное) на англ. и возвращаем перевод на русском
    word_to_translate = str(input('Переводим с англ. на рус.: '))
    # Сохраняем в памяти пришел ли тайтл или строчный
    check_for_title = word_to_translate.istitle()
    # В любом случае приводим к строчной
    word_to_translate = word_to_translate.lower()
    # Проверяем пользователь ввел тайтл или строку
    if check_for_title:
        # Возвращаем в любом случае строчный но если вводили тайтл делаем тайтл
        print(num_translate_adv(word_to_translate).title())
    else:
        # Выводим строчную если вводили строчную
        print(num_translate_adv(word_to_translate))
