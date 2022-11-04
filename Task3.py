dicionary = \
    {
         "Привет":  "Здравстуйте :)"
    }
isstarted = True
while isstarted:
    answer = input("Я: ")
    if answer == 'Выход':
        isstarted = not isstarted
    if answer in dicionary.keys():
        print('Бот-чат:', dicionary[answer])
    else:
        print('Неизветсная команда!')