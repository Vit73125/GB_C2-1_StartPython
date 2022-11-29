# Функции и модули

# Импорт функции
# import

import hello                # Импорт

print(hello.f(1))

# Псевдоним функции

import hello as h           # Псевдоним

print(h.f(1)) 

# Значения по умолчанию

def new_string(symbol, count = 3):  # 3 - Значение по умолчанию
    return symbol * count           # Для строкового значения: соединить строку count раз

print(new_string('!, 5'))
print(new_string('!'))              # Если есть значение по умолчанию, то этот параметр можно не передавать
print(new_string(4))                # Автоматическое приведение типа в функции:
                                    # Для числового значения '*' выполнит умножение

# Передача в функцию произвольного числа аргументов

def concatenatio(*params):                  # * - переменное число параметров
    res = ""                                # Параметры могут быть только строковыми значениями
    for item in params:
        res += item
    return res

print(concatenatio('a', 's', 'd', 'w'))     # asdw - 4 параметра
print(concatenatio('a', '1'))               # a1 - 2 параметра
# print(concatenatio(1, 2, 3, 4))             # Ошибка: в функции параметры использоваться только со строкой
