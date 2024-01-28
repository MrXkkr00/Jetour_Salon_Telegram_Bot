from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardRemove

from data.config import ADMINS
from handlers.users.test_drive import shartnoma
from keyboards.default import contact_button
from keyboards.default.bosh_nemu import bosh_menu, bosh_menu_ru
from keyboards.default.contact_button import contact_keyboard_ru
from loader import dp, bot


class Test_drive_ru(StatesGroup):
    ism = State()
    contact = State()


@dp.message_handler(text="📄Запись на тест драйв")
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(f"Оставьте свое имя и фамилию", reply_markup=ReplyKeyboardRemove())
    await Test_drive_ru.ism.set()


@dp.message_handler(state=Test_drive_ru.ism)
async def ism(message: types.Message, state: FSMContext):
    await state.update_data(
        {"ism": message.text}
    )
    await message.answer(f"Отправить контакт", reply_markup=contact_keyboard_ru)
    await Test_drive_ru.next()


@dp.message_handler(content_types="contact", state=Test_drive_ru.contact)
async def contact(message: types.Message, state: FSMContext):
    data = await state.get_data()
    ism = data.get("ism")
    await message.answer(f"Вы не ошиблись, выбрав нас, \n"
                         f"Наши сотрудники свяжутся с вами в ближайшее время", reply_markup=bosh_menu_ru)
    await bot.send_message(ADMINS[1], f"🙎🏻‍♂Клиент : {ism}\n"
                                      f"🗂задача: 📄Запись на тест драйв.\n"
                                      f"📲контакт : T.me/{message.contact.phone_number}")
    await bot.send_message(ADMINS[0], f"🙎🏻‍♂Клиент : {ism}\n"
                                      f"🗂задача: 📄Запись на тест драйв.\n"
                                      f"📲контакт : T.me/{message.contact.phone_number}")
                                      
    await bot.send_message(ADMINS[2], f"🙎🏻‍♂Клиент : {ism}\n"
                                      f"🗂задача: 📄Запись на тест драйв.\n"
                                      f"📲контакт : T.me/{message.contact.phone_number}")
    await state.finish()







class tex_xiz_ru(StatesGroup):
    ism = State()
    contact = State()


@dp.message_handler(text="⚠️ Запись на ТО")
async def bot_statex1_xizrt(message: types.Message):
    await message.answer(f"Оставьте свое имя и фамилию", reply_markup=ReplyKeyboardRemove())
    await tex_xiz_ru.ism.set()


@dp.message_handler(state=tex_xiz_ru.ism)
async def ismtex_x1iz(message: types.Message, state: FSMContext):
    await state.update_data(
        {"ism": message.text }
    )
    await message.answer(f"Отправить контакт ", reply_markup=contact_keyboard_ru)
    await tex_xiz_ru.next()


@dp.message_handler(content_types="contact",state=tex_xiz_ru.contact)
async def conta11cttex_xiz(message: types.Message, state: FSMContext):
    data = await state.get_data()
    ism = data.get("ism")
    await message.answer(f"Вы не ошиблись, выбрав нас, \n"
                         f"Наши сотрудники свяжутся с вами в ближайшее время", reply_markup=bosh_menu_ru)
    await bot.send_message(ADMINS[1], f"🙎🏻‍♂Клиент : {ism}\n"
                                      f"🗂задача: ⚠️Запись на ТО.\n"
                                      f"📲контакт : T.me/{message.contact.phone_number}")
    await bot.send_message(ADMINS[0], f"🙎🏻‍♂Клиент : {ism}\n"
                                      f"🗂задача: ⚠️Запись на ТО.\n"
                                      f"📲контакт : T.me/{message.contact.phone_number}")
                                      
    await bot.send_message(ADMINS[2], f"🙎🏻‍♂Клиент : {ism}\n"
                                      f"🗂задача: ⚠️Запись на ТО.\n"
                                      f"📲контакт : T.me/{message.contact.phone_number}")
    await state.finish()



class shartnoma_ru(StatesGroup):
    ism = State()
    contact = State()


@dp.message_handler(text="🤝Онлайн заявка на договор")
async def bot_sta1_xizrt(message: types.Message):
    await message.answer(f"Оставьте свое имя и фамилию", reply_markup=ReplyKeyboardRemove())
    await shartnoma_ru.ism.set()


@dp.message_handler(state=shartnoma_ru.ism)
async def ismt_x1iz(message: types.Message, state: FSMContext):
    await state.update_data(
        {"ism": message.text}
    )
    await message.answer(f"Отправить контакт ", reply_markup=contact_keyboard_ru)
    await shartnoma_ru.next()


@dp.message_handler(content_types="contact",state=shartnoma_ru.contact)
async def contttex_xiz(message: types.Message, state: FSMContext):
    data = await state.get_data()
    ism = data.get("ism")
    await message.answer(f"Вы не ошиблись, выбрав нас, \n"
                         f"Наши сотрудники свяжутся с вами в ближайшее время", reply_markup=bosh_menu_ru)
    await bot.send_message(ADMINS[1], f"🙎🏻‍♂Клиент : {ism}\n"
                                      f"🗂задача: 🤝Онлайн заявка на договор\n"
                                      f"📲контакт : T.me/{message.contact.phone_number}")
    await bot.send_message(ADMINS[0], f"🙎🏻‍♂Клиент : {ism}\n"
                                      f"🗂задача: 🤝Онлайн заявка на договор\n"
                                      f"📲контакт : T.me/{message.contact.phone_number}")
                                      
    await bot.send_message(ADMINS[2], f"🙎🏻‍♂Клиент : {ism}\n"
                                      f"🗂задача: 🤝Онлайн заявка на договор\n"
                                      f"📲контакт : T.me/{message.contact.phone_number}")
    await state.finish()

