#Модули Python
#Модули - это python код на котором мы пишем фунции и т.д
#В Python импортировать модули можно несколькими способами (3):
#1 - импортировать сам модуль
# import moduls #без окончания .py
# print(moduls.reverse_integer(451))
# print(moduls.reverse_list([10, 11, 3]))

# # #2 - импортировать отдельные определения из модуля
# from moduls import reverse_integer, reverse_list

# print(reverse_integer(578))
# print(reverse_list([90, 30, 10]))

# #3 - импортировать всё содержимое модуля сразу
# from moduls import *
# print(reverse_integer(432123))
# print(reverse_list([10, 0.1, True, "Hello"]))

# from moduls import mult, it 

# print(mult(10, 20))
# print(it)

#Работа с файлами Python
# f = open('test.txt', 'w')
# f.write("Hello World and Geeks Python")
# f.close()

# r = open('test.txt', 'r')
# print(r.read())
# r.close()

# py = open('test.py', 'w')
# py.write("print('Hello World')")
# py.close()

# read_python_file = open('moduls.py', 'r')
# print(read_python_file.read())
# read_python_file.close()

# rus = open('rus.txt', 'w', encoding='utf-8')
# rus.write("Привет всем!")
# rus.close()

# read_rus = open('rus.txt', 'r', encoding='utf-8')
# print(read_rus.read())
# read_rus.close()

# with open('with.txt', 'w', encoding='utf-8') as n:
#     n.write("Этот файл можно и не закрывать")

# with open('with.txt', 'r', encoding='utf-8') as r:
#     print(r.read())