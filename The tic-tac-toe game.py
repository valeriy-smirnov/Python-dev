import main_game
print('Добро пожаловать в игру «Крестики-нолики»:')
menu = ['1. Играть с другом', '2. Играть с компьютером', '3. Выйти']

while True:
    print('Список доступных команд:')
    for i in range(len(menu)):
        print(menu[i])
    while True: # Защита от ввода не числа
        command = input('Введите номер команды: ')
        try:
            command = int(command)
            break
        except:
            print('Введите пункт из меню!')
    if 1 <= command <= 3:
        print(f'Вы выбрали: {menu[command-1][3:]}')
    if command == 1:
        main_game.tic_tac_toe()
    if command == 2:
        main_game.tic_tac_toe(computer=True)
    if command == 3:
        break
    