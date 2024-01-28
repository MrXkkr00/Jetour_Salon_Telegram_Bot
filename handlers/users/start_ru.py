from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import InputFile

from keyboards.default.bosh_nemu import bosh_menu, bosh_menu_ru, modellar_uz_ru, modellar_ru
from loader import dp, bot




@dp.message_handler(text="📍Адрес")
async def bot_start(message: types.Message):
    lat = "41.206294"
    lon = "69.221745"
    # reply = "latitude:  {}\nlongitude: {}".format(lat, lon)
    await bot.send_location(984568970, lat, lon)
    await message.answer(text=f"Сергели 2-й квартал, 5-я станция метро 'Jetour' автосалон",reply_markup=bosh_menu)











@dp.message_handler(text="🇷🇺🔄")
@dp.message_handler(text="🏠 Главное меню")
async def bot_start_ru(message: types.Message):
    await message.answer(f"Ассаляму Алейкум, {message.from_user.full_name}!\nДобро пожаловать в наш бот",reply_markup=bosh_menu_ru)


@dp.message_handler(text="💵 Прайс-лист")
async def bot_start(message: types.Message):
    # await bot.send_location(message.from_user.id, InputFile("Цены.xls"))
    await message.answer_document(InputFile("./data/Цены.xls"))


@dp.message_handler(text="☎️ Связаться с нами")
async def bot_start(message: types.Message):
    await message.answer(f"Наши контактные телефоны\n78 113 03 00\n91 033 30 03 \n99 305 03 30 \n77 041 30 03\n77 042 "
                         f"30 03")


@dp.message_handler(text="🏎Информация о наших автомобилях")
async def bot_start(message: types.Message):
    await message.answer(f"Model turini tanlang",
                         reply_markup=modellar_ru)


@dp.message_handler(text="🏢 О компании")
async def bot_sgbtart(message: types.Message):
    await message.answer(f"Компания Джетур создана в 2018 году на базе хостинговой компании, созданной в 1997 году"
                         f" найден. Основной вид деятельности — производство семейных кроссоверов, предназначенных для путешествий"
                         f"Китайское название бренда произносится как 'Jietu', и лучший перевод на узбекский язык — "
                         f" означает 'Дорога Победы'. Весь ассортимент продукции Jetour — 5-, 6- или 7-местный."
                         f" предназначен для среднего сегмента с вариантами комплектации, при этом внутреннего сгорания"
                         f"производство электрических, полностью электрических, подключаемых гибридов, а в будущем и водородных автомобилей"
                         f" предусматривает. Семейный внедорожник Jetour X70S будет представлен на Пекинском автосалоне в январе 2018 года."
                         f" и представил концепт-кары Jetour X. В том же году ежемесячные продажи X70 составили "
                         f" добился увеличения с 10 000 единиц. В 2019 году продажи успешно выросли со 134 000 единиц"
                         f" увеличивается, и таким образом компания Jetour с высокой скоростью выходит на крупные рынки."
                         f"Объем продаж превысил 300 000 единиц и стал первым Китаем, достигшим объема продаж 300 000 за 28 месяцев"
                         f" бренда. До июля 2022 года Jetour вошёл более чем в 30 стран мира и в 700"
                         f" имеет почти миллион клиентов. Общее количество официальной дилерской сети Jetour превысило 300"
                         f" и ожидается, что к концу 2025 года оно достигнет 1500. В настоящее время компания имеет X90"
                         f"PLUS, Shanghai L9, Traveler, X70 PLUS, X70, Dashing и др. представили уже десятки моделей."
                         f"Название бренда представляет собой сочетание английских слов JET (самолет) и TOUR (путешествие)"
                         f"Это делает путешествие на автомобиле таким же приятным, как полет на частном самолете, и это чрезвычайно "
                         f" означает, что это может быть удобно. Бренд неустанно работает в различных областях и, наконец, "
                         f"люди, достигающие своих целей, открывающие новые горизонты и стремящиеся к счастливой гармоничной жизни"
                         f" предназначено для.")
