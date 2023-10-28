#Functions - функции Python
# def hello():
#     print("Hello World")
# hello() #вызов функции по имени hello()

# def add():
#     num1 = input("Введите первое число: ")
#     num2 = input("Введите второе число: ")
#     print(int(num1) + int(num2))
# # add()

# def reverse_name():
#     name = input("Введите свое имя: ")
#     print(name[::-1])
# # reverse_name()

# print(len("Hello"))
# print(len([1, "Hello", True, 0.1]))

# def sub(num1, num2): #num1, num2 - параметры функции
#     print(num1 - num2)
# sub(20, 10) #20, 10 - аргументы функции
# sub(100, 88)
# sub(100, 200)

# def calculator(num1, num2, operator):
#     if operator == "+":
#         print(num1 + num2)
#     elif operator == "-":
#         print(num1 - num2)
#     elif operator == "*":
#         print(num1 * num2)
#     elif operator == "/":
#         print(num1 / num2)
#     else:
#         print("Такого оператора нету")

# calculator(10, 50, "+")
# calculator(200, 100, "-")
# calculator(100, 30, "*")
# calculator(500, 2, "/")
# calculator(10, 10, "**")

# def div(num1:int, num2:int):
#     try:
#         print(num1 / num2)
#     except ZeroDivisionError:
#         print("Деление на ноль")
# div(10, 2)
# div(100, 0)
# div(10.0, 3.0)

# def mult(num1:int=10, num2:int=10) -> int:
#     "Эта функция для умножения чисел num1 и num2"
#     print(num1 * num2)
# mult(20, 1)

# number = 72
# print(number[::-1])

word = "Кыргызская Республика" #КР
word = "For your interest" #FYI
split_word = word.split()
print(split_word)
result = ""
for sul in split_word:
    print(sul)
    result += sul[0]
print(result)