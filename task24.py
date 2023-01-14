# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит заданное количество конфет.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'
from random import randint

player_name = input('Введите Ваше имя: ')
bot = 'Bot'
sweet_amount = int(input("Укажите изначальное количество конфет: "))
taken_sweets = 0
random_turn = randint(1, 2)
win = False
max_taken_sweet = 28


def change_turn():
    global random_turn
    if random_turn == 1:
        random_turn = 2
    else:
        random_turn = 1


def player_turn():
    global taken_sweets, sweet_amount, max_taken_sweet
    taken_sweets = int(input('Сколько конфет Вы хотите взять? '))
    while taken_sweets > max_taken_sweet:
        taken_sweets = int(
            input(f'Можно взять количество меньшее чем {max_taken_sweet}. Так какое количество конфет хотите взять? '))
    sweet_amount = sweet_amount - taken_sweets
    print(f'Осталось {sweet_amount} конфет')


def smart_bot_turn():
    global sweet_amount, taken_sweets, max_taken_sweet
    if sweet_amount >= 29:
        if sweet_amount-max_taken_sweet<=max_taken_sweet:
            taken_sweets = randint(1, sweet_amount-max_taken_sweet-1)
        else:
            taken_sweets = randint((sweet_amount - 29) % 29, 28)
    elif sweet_amount == max_taken_sweet:
        taken_sweets = max_taken_sweet
    else:
        taken_sweets = sweet_amount
    print(f'Бот взял {taken_sweets} конфет')
    sweet_amount = sweet_amount - taken_sweets
    print(f'Осталось {sweet_amount} конфет')


def game():

    winner = ''
    while sweet_amount > 0:
        if random_turn == 1:
            player_turn()
        else:
            smart_bot_turn()
        if sweet_amount == 0:
            winner = player_name if random_turn == 1 else bot
            print(f'Выиграл {winner}')
        else:
            change_turn()


game()
