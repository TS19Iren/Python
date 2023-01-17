from tkinter import *
import random

main_field = Tk()
main_field.title('Крестики-нолики')
field = []
background_color = 'light blue'
moves_count = 0
is_game_over = False
label = Label(main_field, text='')


def game():
    prepare_field()
    main_field.mainloop()


def game_move(symbol, x_pos, y_pos):
    field[x_pos][y_pos]['text'] = symbol
    global moves_count
    moves_count += 1


def check_pos_for_bot(but_1, but_2, but_3):
    if (but_1['text'] == 'O' and but_2['text'] == 'O' and but_3['text'] == ' ') \
            or (but_1['text'] == 'O' and but_2['text'] == ' ' and but_3['text'] == 'O') \
            or (but_1['text'] == ' ' and but_2['text'] == 'O' and but_3['text'] == 'O'):
        return True
    return False


def put_symbol(but_1, but_2, but_3, symbol):
    if but_1['text'] == ' ':
        but_1['text'] = symbol
    elif but_2['text'] == ' ':
        but_2['text'] = symbol
    else:
        but_3['text'] = symbol
    global moves_count
    moves_count += 1


def bot_turn():
    for i in range(3):
        # проверка строк
        if (check_pos_for_bot(field[i][0], field[i][1], field[i][2])):
            put_symbol(field[i][0], field[i][1], field[i][2], 'O')
        # проверка столбцов
        if (check_pos_for_bot(field[0][i], field[1][i], field[2][i])):
            put_symbol(field[0][i], field[1][i], field[2][i], 'O')
        # проверка диагоналей
        if (check_pos_for_bot(field[0][0], field[1][1], field[2][2])):
            put_symbol(field[0][0], field[1][1], field[2][2], 'O')
        if (check_pos_for_bot(field[2][0], field[1][1], field[0][2])):
            put_symbol(field[2][0], field[1][1], field[0][2], 'O')
        if check_win('O'):
            global is_game_over
            is_game_over = True
            return

    x_pos = random.randint(0, 2)
    y_pos = random.randint(0, 2)
    while not can_move(x_pos, y_pos):
        x_pos = random.randint(0, 2)
        y_pos = random.randint(0, 2)
    field[x_pos][y_pos]['text'] = 'O'


def can_move(x_pos, y_pos):
    global is_game_over
    return not is_game_over and field[x_pos][y_pos]['text'] == ' '


def end_game(smb):
    global is_game_over
    is_game_over = True
    if smb == 'X':
        label['text'] = 'Вы победили!'
    else:
        label['text'] = 'Бот победил!'


def player_turn(x_pos, y_pos):
    if can_move(x_pos, y_pos):
        game_move('X', x_pos, y_pos)
        if check_win('X'):
            end_game('X')
        if not is_game_over and moves_count < 5:
            bot_turn()
            if check_win('O'):
                end_game('O')
    return


def check_win(symbol):
    for i in range(3):
        # проверка строк
        if field[i][0]['text'] == symbol and field[i][1]['text'] == symbol and field[i][2]['text'] == symbol:
            return True
        # проверка столбцов
        if field[0][i]['text'] == symbol and field[1][i]['text'] == symbol and field[2][i]['text'] == symbol:
            return True
        # проверка диагоналей
    if (field[0][0]['text'] == symbol and field[1][1]['text'] == symbol and field[2][2]['text'] == symbol) \
            or (field[2][0]['text'] == symbol and field[1][1]['text'] == symbol and field[0][2]['text'] == symbol):
        return True


def prepare_field():
    global main_field
    for row in range(3):
        line = []
        for col in range(3):
            button = Button(main_field, text=' ', width=4, height=2,
                            font=('Verdana', 20, 'bold'),
                            background=background_color,
                            command=lambda row=row, col=col: player_turn(row, col))
            button.grid(row=row, column=col, sticky='nsew')
            line.append(button)
        field.append(line)
    new_game_btn = Button(main_field, text='new game', command=new_game)
    new_game_btn.grid(row=3, column=0, columnspan=3, sticky='nsew')

    global label
    label.grid(row=4, column=0, columnspan=3, sticky='nsew')


# Логика кнопки "новая игра". Сбрасываются все свойства кнопок.
def new_game():
    global background_color
    for row in range(3):
        for col in range(3):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = background_color
    global is_game_over, moves_count, label
    is_game_over = False
    moves_count = 0
    label['text'] = ''


game()
