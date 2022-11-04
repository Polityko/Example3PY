# Задача 1. Создайте файл. Запишите в него N первых элементов последовательности Фибоначчи.
num1 = 0
num2 = 1
count = 7

data = open('fibonacci.txt', 'w')
for i in range(count):
    data.writelines(str(num1) + '\n')
    (num1, num2) = (num2, num1 + num2)
    print(num1)