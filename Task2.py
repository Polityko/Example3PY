with open('fruits.txt', encoding='utf-8') as data:
    fruits = data.readline().split()
    print(fruits)
    letter = str(input('Введите букву: '))
    for fruct in fruits:
        if fruct[0] == letter:
            print(fruct)