#Циклы for, while
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# ###########
# for number in range(1001):
#     print(number)

# for py in range(1, 101):
#     print("Python", py)

# names = ["Kurmanbek", "Nurbolot", "Beksultan", "Daniel", "Emir", "Bay"]
# print("Здравствуйте", names[0])
# print("Здравствуйте", names[1])
# print("Здравствуйте", names[2])
# print("Здравствуйте", names[3])
# print("Здравствуйте", names[4])
# print("=================================")
# for name in names:
#     print("Здравствуйте", name)

# numbers = [10, 1, 3, 4, 5, 1001, 400, 505, 2, 3, 555]
# print(numbers)
# for number in numbers:
#     if number % 2 == 0:
#         print(number, "четный")
#     else:
#         print(number, "нечетный")

# nums = [] #пустой список
# print(nums)
# for num in range(1, 100, 2): #1 - начало, 100 - конец, 2 - шаг
#     nums.append(num) #добавляем цифры в пустой список nums
# print(nums) #выводим результат

# client = ["Nurs", "Nur", "Beka", "Bayas", "Dior", "Syimyk", "Islam"]
# find_client = input("Кого искать? ")
# for find in client:
#     if find == find_client:
#         print(find_client, "найден")
#         break #прерывает цикл и выходит из него
#     else:
#         print("Ищем клиента...")

# name = "Nurbolot"
# for n in name:
#     print(n)

# cars = ("BMW", "Lexus", "Toyota", "Tesla")
# for car in cars:
#     print(car)

# num1 = 10
# num2 = 20
# while num1 < num2:
#     num1 += 1
#     print(num1)

# n = 0
# while True:
#     n += 1
#     print("Geeks", n)

#Генератор паролей Python
# import random

# letters = "qwertyuiopasdfghjklzxcvbnm1234567890"
# for n in range(20):
#     result = ""
#     for i in range(8):
#         random_letter = random.choice(letters)
#         result += random_letter
#     print(result)