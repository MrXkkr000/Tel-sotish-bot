from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.choice import sim_kart,Memory,color
from loader import dp


@dp.message_handler(text='Owner')
async def bot_s2tart(message: types.Message):
    await message.answer(f" Bu bot Rasulbek Qadomboyev tomonidan yasalgan \nMurojat uchun @QRasulbek")
