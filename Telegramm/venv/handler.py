import logging

from aiogram import types

import game_config
import game_logic
import keyboard
from create import dp
from game_states import Game_state
import logging.config

global state, total

logging.basicConfig(filename='log.log', encoding='utf-8', level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': True,
})


@dp.message_handler(commands=['start'])
async def mes_start(message: types.Message):
    logging.info("Принята команда START")
    logging.debug(f'Пришло сообщение {message}')

    global state
    state = Game_state.START
    logging.debug(f'установлено состояние {state}')
    await message.answer("Игра конфетки!", reply_markup=keyboard.get_start_keyboard())


@dp.message_handler(lambda message: message.text == "Установить начальное количество конфет")
async def set_candies_count(message: types.Message):
    logging.info('Установка количества конфет')
    logging.debug(f'Пришло сообщение {message}')

    global state
    state = Game_state.INIT_GAME
    logging.debug(f'установлено состояние {state}')
    await message.answer("Сколько было конфет изначально?")


@dp.message_handler()
async def mes_all(message: types.Message):
    logging.debug(f'Пришло сообщение {message}')
    global total, state
    try:
        state
    except NameError:
        state = Game_state.START
        logging.debug(f'установлено состояние {state}')

    match state:
        case Game_state.START:
            await message.answer("Игра конфетки!", reply_markup=keyboard.get_start_keyboard())
        case Game_state.INIT_GAME:
            await set_candies_and_dice(message)
        case Game_state.GAME_IN_PROGRESS:
            if game_logic.validate_answer(message.text, game_config.max_taken_sweets):
                logging.debug(f'Пользователь взял {message.text} конфет')
                total = game_logic.left_sweets(int(message.text), total)
                logging.debug(f'Осталось {total} конфет')

                if game_logic.check_end_game(total):
                    state = Game_state.END_GAME
                    logging.debug(f'установлено состояние {state}')
                    await message.answer(f'Ура, ты победил!', reply_markup=keyboard.restart_keyboard())
                    return
                else:
                    await message.answer(f'На столе осталось {total} конфет')
                bot_taken_sweets = game_logic.smart_bot_turn(total)
                logging.debug(f'Бот взял {bot_taken_sweets} конфет')
                total = game_logic.left_sweets(bot_taken_sweets, total)
                logging.debug(f'Осталось {total} конфет')
                await message.answer(f'Бот взял {bot_taken_sweets}. На столе осталось {total} конфет')
                if game_logic.check_end_game(total):
                    state = Game_state.END_GAME
                    logging.debug(f'установлено состояние {state}')
                    await message.answer(f'Бот победил!', reply_markup=keyboard.restart_keyboard())
                    return

            else:
                logging.warning(f'Введено не валидное значение: {message.text}')
                await message.answer(game_logic.get_rnd_answer_when_not_valid())
        case Game_state.END_GAME:
            state = Game_state.START
            logging.debug(f'установлено состояние {state}')

            await message.answer(text='Играем снова', reply_markup=keyboard.get_start_keyboard())


async def set_candies_and_dice(message: types.Message):
    logging.info('Установка количества конфет и выбор хода')
    global state, total
    if message.text.isdigit() and int(message.text) > 0:
        total = int(message.text)
        logging.debug(f'Начальное количество конфет {total}')
        await message.answer(f"На столе {total} конфет")
        msg_dice = await message.answer_dice()
        logging.debug(f'На кубике выпало {msg_dice.dice.value}')
        state = Game_state.GAME_IN_PROGRESS
        logging.debug(f'установлено состояние {state}')

        if msg_dice.dice.value % 2 == 0:
            await message.answer(f'Бог рандома решил, что ты будешь ходить первым. Сколько будешь брать?')
        else:
            await message.answer(f'Бог рандома решил, что первым будет ходить бот')
            taken_sweets = game_logic.smart_bot_turn(total)
            total = game_logic.left_sweets(taken_sweets, total)
            await message.answer(f'Бот взял {taken_sweets} конфет. Осталось {total}. Сколько конфет берешь?')
    else:
        await message.answer("Введите число")
