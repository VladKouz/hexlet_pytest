from src.capitalize import capitalize

'''Тесты для функции capitalize (первая версия)
if capitalize("hello") != "Hello":
    raise Exception("Функция работает неверно!")

if capitalize("") != "":
    raise Exception("Функция работает неверно!")

print("Все тесты пройдены!")

'''

'''Тесты для функции capitalize (через assert)'''
assert capitalize("") == ""
assert capitalize("hello") == "Hello"


#PYTHONPATH=src python3 tests/test_capitalize.py