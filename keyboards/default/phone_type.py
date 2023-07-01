from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

iPhone14 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="iPhone 14"),
            KeyboardButton(text="iPhone 14 Plus")
        ],
        [
            KeyboardButton(text="iPhone 14 Pro"),
            KeyboardButton(text="iPhone 14 Pro Max")
        ],

    ],
    resize_keyboard=True
)

iPhone13 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="iPhone 13 Mini"),
            KeyboardButton(text="iPhone 13")
        ],
        [
            KeyboardButton(text="iPhone 13 Pro"),
            KeyboardButton(text="iPhone 13 Pro Max")
        ],

    ],
    resize_keyboard=True
)


iPhone12 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="iPhone 12 Mini"),
            KeyboardButton(text="iPhone 12 ")
        ],
        [
            KeyboardButton(text="iPhone 12 Pro"),
            KeyboardButton(text="iPhone 12 Pro Max")
        ],

    ],
    resize_keyboard=True
)


iPhone11 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="iPhone 11")
        ],

    ],
    resize_keyboard=True
)