from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

bosh_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🏎Avtomobillarimiz haqida ma'lumotlar"),
        ],
        [
            KeyboardButton(text='🤝Shartnoma uchun onlayn ariza'),
            KeyboardButton(text="💵 Narxlar jadvali"),
        ],
        [
            KeyboardButton(text="📄Test drivega ro'yxatdan o'tish"),
            KeyboardButton(text="⚠️ Texnik xizmatga yozilish"),
        ],
        [
            KeyboardButton(text='🏢 Kompaniyamiz haqida'),
            KeyboardButton(text="☎️ Biz bilan aloqa"),
        ],
        [
            KeyboardButton(text='📍Manzil'),
            KeyboardButton(text="🇷🇺🔄"),
        ],
    ],
    resize_keyboard=True
)

biz_bilan_aloqa = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📝 Fikr qoldirish")
        ],
        [
            KeyboardButton(text="🏡 Asosiy menyu")
        ],
    ],
    resize_keyboard=True
)

kontactlar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📍️ Dilerlar")
        ],
        [
            KeyboardButton(text="👔 Kia Uzbekistan aloqa markazi")
        ],
        [
            KeyboardButton(text="🏡 Asosiy menyu")
        ],
    ],
    resize_keyboard=True
)














bosh_menu_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🏎Информация о наших автомобилях"),
        ],
        [
            KeyboardButton(text='🤝Онлайн заявка на договор'),
            KeyboardButton(text="💵 Прайс-лист"),
        ],
        [
            KeyboardButton(text="📄Запись на тест драйв"),
            KeyboardButton(text="⚠️ Запись на ТО"),
        ],
        [
            KeyboardButton(text='🏢 О компании'),
            KeyboardButton(text="☎️ Связаться с нами"),
        ],
        [
            KeyboardButton(text="📍Адрес"),
            KeyboardButton(text="🇺🇿🔄"),
        ],
    ],
    resize_keyboard=True
)

modellar_uz_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="JETOUR"),
            KeyboardButton(text="BESTUNE"),
        ],
        [
            KeyboardButton(text="HONGQI"),
            KeyboardButton(text="DONGFENG")
        ],
        [
            KeyboardButton(text="AIQAR"),
            KeyboardButton(text="SHINERAY")
        ],
        [
            KeyboardButton(text="🏠 Asosiy menu"),
        ]
    ],
    resize_keyboard=True
)

modellar_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="JETOUR"),
            KeyboardButton(text="BESTUNE"),
        ],
        [
            KeyboardButton(text="HONGQI"),
            KeyboardButton(text="DONGFENG")
        ],
        [
            KeyboardButton(text="AIQAR"),
            KeyboardButton(text="SHINERAY")
        ],
        [
            KeyboardButton(text="🏠 Главное меню"),
        ]
    ],
    resize_keyboard=True
)