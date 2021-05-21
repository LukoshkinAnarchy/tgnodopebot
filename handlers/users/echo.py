from aiogram import types
from loader import dp
from handlers.users.no import get_answer


# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@dp.message_handler()
async def bot_echo(message: types.Message):
    #    await message.answer(f"({get_answer({message.text})}")
    #    await message.answer(f"{get_answer({message.text})}")
    await message.answer(f"Нет блять, {get_answer(f'{message.text}')}")
