###
import random

def check_winner(s: list):
    """This function determines if one of the players won.

    The function takes the current list of played squares and tries to match it with the winning combination. If the function is able to find one, it returns the value of the square (the winner).
     
    Args:
        s (list): The list that represents the game field with its current state.

    Returns:
        The function returns the winner; if nobody has won yet, it returns None
    """
    for i in range(3):
        if s[i][0] == s[i][1] == s[i][2] and s[i][0] != '-':
            return s[i][1]
        elif s[0][i] == s[1][i] == s[2][i] and s[0][i] != '-':
            return s[0][i]
        elif (s[0][0] == s[1][1] == s[2][2] and s[1][1] != '-') or (s[2][0] == s[1][1] == s[0][2] and s[1][1] != '-'):
            return s[1][1]        
    return None

def tic_tac_toe(computer=False):
    """This function is a tic-tac-toe game.
    
    The function is preparing the field, then it asks each player for coordinates (x,y), checks them and places the sign.
    If there are more than 4 moves, the function tries to check the winner.

    Args:
        computer: Default is False. If True, randomly choose coordinates as "O".
        
    Raises:
        TypeError: Raise exception to force player to reenter correct coordinates.
    """
    # Preps
    s=[[],[],[]]
    for i in range(3):
        for j in range(3):
            s[i].append('-')
    move = 0
    list_xy = {'X':[],'O':[]}
    # Main game cycle
    while move < 9:
        field= f'''             0    1    2
        0    {s[0][0]}    {s[1][0]}    {s[2][0]}
        1    {s[0][1]}    {s[1][1]}    {s[2][1]}
        2    {s[0][2]}    {s[1][2]}    {s[2][2]}'''
        print(field)
        turn = 'X' if move % 2 ==0 else 'O'
        if computer == False or turn == 'X':
            coord = input(f'Введите координаты "{turn}" в формате двух чисел через пробел: ')
        else:
            coord = f'{random.randint(0,2)} {random.randint(0,2)}'
        try:
            x = int(coord.split()[0])
            y = int(coord.split()[1])
            if 0<= x <= 2 and 0<= y <= 2 and s[x][y] == '-':
                s[x][y] = turn
                move += 1
                #list_xy[turn].append((x,y))
            else:
                raise TypeError       
        except:
            print('Введены не верные координаты или поле уже занято')
        if move >= 5:
            w = check_winner(s)
            if w != None:
                print(field)
                print(f'Поздравляем "{w}" с заслуженной победой!')
                break
    else:
        print("Игра закончилась в ничью!")
        print(field)