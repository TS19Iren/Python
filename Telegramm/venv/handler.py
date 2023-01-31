import emoji
import game_logic, game_config
from create import dp
from aiogram import types
import keyboard
from game_states import Game_state

global state, total


@dp.message_handler(commands=['start'])
async def mes_start(message: types.Message):
    global state
    state = Game_state.START
    await message.answer("Игра конфетки!", reply_markup=keyboard.get_start_keyboard())


@dp.message_handler(lambda message: message.text == "Установить начальное количество конфет")
async def set_candies_count(message: types.Message):
    global state
    state = Game_state.INIT_GAME
    await message.answer("Сколько было конфет изначально?")


@dp.message_handler()
async def mes_all(message: types.Message):
    global total, state
    try:
        state
    except NameError:
        state = Game_state.START
    match state:
        case Game_state.START:
            await message.answer("Игра конфетки!", reply_markup=keyboard.get_start_keyboard())
        case Game_state.INIT_GAME:
            await set_candies_and_dice(message)
        case Game_state.GAME_IN_PROGRESS:
            if game_logic.validate_answer(message.text, game_config.max_taken_sweets):
                total = game_logic.left_sweets(int(message.text), total)
                if game_logic.check_end_game(total):
                    state = Game_state.END_GAME
                    await message.answer(f'Ура, ты победил!', reply_markup=keyboard.restart_keyboard())
                    return

                else:
                    await message.answer(f'На столе осталось {total} конфет')

                bot_taken_sweets = game_logic.smart_bot_turn(total)
                total = game_logic.left_sweets(bot_taken_sweets, total)
                await message.answer(f'Бот взял {bot_taken_sweets}. На столе осталось {total} конфет')
                if game_logic.check_end_game(total):
                    state = Game_state.END_GAME
                    await message.answer(f'Бот победил!', reply_markup=keyboard.restart_keyboard())
                    return

            else:
                await message.answer(game_logic.get_rnd_answer_when_not_valid())
        case Game_state.END_GAME:
            state = Game_state.START
            await message.answer(text='Играем снова', reply_markup=keyboard.get_start_keyboard())


async def set_candies_and_dice(message: types.Message):
    global state, total
    if message.text.isdigit() and int(message.text) > 0:
        total = int(message.text)
        await message.answer(f"На столе {total} конфет")
        msg_dice = await message.answer_dice()
        state = Game_state.GAME_IN_PROGRESS
        if msg_dice.dice.value % 2 == 0:
            await message.answer(f'Бог рандома решил, что ты будешь ходить первым. Сколько будешь брать?')
        else:
            await message.answer(f'Бог рандома решил, что первым будет ходить бот')
            taken_sweets = game_logic.smart_bot_turn(total)
            total = game_logic.left_sweets(taken_sweets, total)
            await message.answer(f'Бот взял {taken_sweets} конфет. Осталось {total}. Сколько конфет берешь?')
    else:
        await message.answer("Введите число")


@dp.message_handler()
async def mes_settings(message: types.Message):
    global total
    count = int(message.text.split()[1])
    total = count
    await message.answer(f'Максимальное количество конфет установлено {total}')
