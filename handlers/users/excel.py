from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ContentType

from keyboards.default.choice import sim_kart, Memory, color
from loader import dp


@dp.message_handler(content_types=ContentType.DOCUMENT)
async def bot_excel(message: types.Message):
    await message.document.download(destination_file="data/Excel_File.xlsx", )
    await message.answer(f"Sizning yangi excel faylingiz qabul qilindi!", reply_markup=sim_kart)
