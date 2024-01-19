from aiogram import types, Dispatcher
from configuration import bot

async def click_start(msg: types.Message):
    await bot.send_message(
        chat_id=msg.from_user.id,
        text=f"HI {msg.from_user.first_name}"
    )

def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(click_start, commands=['start'])


