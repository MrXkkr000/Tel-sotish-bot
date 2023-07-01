from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

gb1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1 TB"),
            KeyboardButton(text="512 GB")
        ],
        [
            KeyboardButton(text="256 GB"),
            KeyboardButton(text="128 GB")
        ],

    ],
    resize_keyboard=True
)


gb512 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="512 GB"),
        ],
        [
            KeyboardButton(text="256 GB"),
            KeyboardButton(text="128 GB")
        ],

    ],
    resize_keyboard=True
)


gb256 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="256 GB"),
        ],
        [
            KeyboardButton(text="128 GB"),
            KeyboardButton(text="64 GB")
        ],

    ],
    resize_keyboard=True
)

gb64 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="64 GB")
        ],

    ],
    resize_keyboard=True
)