from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


jetour_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="X90plus"),
            KeyboardButton(text="X70plus")
        ],
        [
            KeyboardButton(text="X70"),
            KeyboardButton(text="Dashing")
        ],
    ],
    resize_keyboard=True
)


hongqi_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Hongqi EQM5"),
            KeyboardButton(text="Hongqi EHS9")
        ],
        [
            KeyboardButton(text="Hongqi H9"),
            KeyboardButton(text="Hongqi H5")
        ],
        [
            KeyboardButton(text="Hongqi HS5"),
        ],
    ],
    resize_keyboard=True
)

dongfeng_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Aeolus Huge"),
            KeyboardButton(text="Aeolus A60")
        ],
        [
            KeyboardButton(text="Forthing T5 evo"),
            KeyboardButton(text="Fengon S508 evr H5")
        ],
        [
            KeyboardButton(text="Hongqi HS5"),
        ],
    ],
    resize_keyboard=True
)