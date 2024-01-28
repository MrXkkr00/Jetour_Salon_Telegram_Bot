from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardRemove

from data.config import ADMINS
from keyboards.default import contact_button
from keyboards.default.bosh_nemu import bosh_menu
from keyboards.default.contact_button import contact_keyboard
from loader import dp, bot


class Test_drive(StatesGroup):
    ism = State()
    contact = State()


@dp.message_handler(text="📄Test drivega ro'yxatdan o'tish")
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(f"Ism Familyangizni qoldiring", reply_markup=ReplyKeyboardRemove())
    await Test_drive.ism.set()

@dp.message_handler(state=Test_drive.ism)
async def ism(message: types.Message, state: FSMContext):
    await state.update_data(
        {"ism": message.text }
    )
    await message.answer(f"Contact yuboring ", reply_markup=contact_keyboard)
    await Test_drive.next()


@dp.message_handler(content_types="contact",state=Test_drive.contact)
async def contact(message: types.Message, state: FSMContext):
    data = await state.get_data()
    ism = data.get("ism")
    await message.answer(f"Bizni tanlab adashmadingiz, \n"
                         f"Xodimlarimiz tez orada sizga aloqaga chiqishadi", reply_markup=bosh_menu)
    await bot.send_message(ADMINS[1], f"🙎🏻‍♂Mijoz : {ism}\n"
                                      f"🗂vazifa: 📄Test drivega yozilish.\n"
                                      f"📲contact : T.me/{message.contact.phone_number}")
    await bot.send_message(ADMINS[0], f"🙎🏻‍♂Mijoz : {ism}\n"
                                      f"🗂vazifa: 📄Test drivega yozilish.\n"
                                      f"📲contact : T.me/{message.contact.phone_number}")
    await bot.send_message(ADMINS[2], f"🙎🏻‍♂Mijoz : {ism}\n"
                                      f"🗂vazifa: 📄Test drivega yozilish.\n"
                                      f"📲contact : T.me/{message.contact.phone_number}")
    await state.finish()







class tex_xiz(StatesGroup):
    ism = State()
    contact = State()


@dp.message_handler(text="⚠️ Texnik xizmatga yozilish")
async def bot_statex_xizrt(message: types.Message):
    await message.answer(f"Ism Familyangizni qoldiring", reply_markup=ReplyKeyboardRemove())
    await tex_xiz.ism.set()


@dp.message_handler(state=tex_xiz.ism)
async def ismtex_xiz(message: types.Message, state: FSMContext):
    await state.update_data(
        {"ism": message.text }
    )
    await message.answer(f"Contact yuboring ", reply_markup=contact_keyboard)
    await tex_xiz.next()


@dp.message_handler(content_types="contact",state=tex_xiz.contact)
async def contacttex_xiz(message: types.Message, state: FSMContext):
    data = await state.get_data()
    ism = data.get("ism")
    await message.answer(f"Bizni tanlab adashmadingiz, \n"
                         f"Xodimlarimiz tez orada sizga aloqaga chiqishadi", reply_markup=bosh_menu)
    await bot.send_message(ADMINS[1], f"🙎🏻‍♂Mijoz : {ism}\n"
                                      f"🗂vazifa: ⚠️Texnik Xizmatga yozilish.\n"
                                      f"📲contact : T.me/{message.contact.phone_number}")
    await bot.send_message(ADMINS[0], f"🙎🏻‍♂Mijoz : {ism}\n"
                                      f"🗂vazifa: ⚠️Texnik Xizmatga yozilish.\n"
                                      f"📲contact : T.me/{message.contact.phone_number}")
    await bot.send_message(ADMINS[2], f"🙎🏻‍♂Mijoz : {ism}\n"
                                      f"🗂vazifa: ⚠️Texnik Xizmatga yozilish.\n"
                                      f"📲contact : T.me/{message.contact.phone_number}")
    await state.finish()




class shartnoma(StatesGroup):
    ism = State()
    contact = State()


@dp.message_handler(text="🤝Shartnoma uchun onlayn ariza")
async def bot_statex_x1izrt(message: types.Message):
    await message.answer(f"Ism Familyangizni qoldiring", reply_markup=ReplyKeyboardRemove())
    await shartnoma.ism.set()


@dp.message_handler(state=shartnoma.ism)
async def ismtex_x1iz(message: types.Message, state: FSMContext):
    await state.update_data(
        {"ism": message.text}
    )
    await message.answer(f"Contact yuboring ", reply_markup=contact_keyboard)
    await shartnoma.next()


@dp.message_handler(content_types="contact", state=shartnoma.contact)
async def contactt1ex_xiz(message: types.Message, state: FSMContext):
    data = await state.get_data()
    ism = data.get("ism")
    await message.answer(f"Bizni tanlab adashmadingiz, \n"
                         f"Xodimlarimiz tez orada sizga aloqaga chiqishadi", reply_markup=bosh_menu)
    await bot.send_message(ADMINS[1], f"🙎🏻‍♂Mijoz : {ism}\n"
                                 f"🗂vazifa:🤝Shartnoma uchun onlayn ariza.\n"
                                      f"📲contact : T.me/{message.contact.phone_number}")
    await bot.send_message(ADMINS[0], f"🙎🏻‍♂Mijoz : {ism}\n"
                                 f"🗂vazifa:🤝Shartnoma uchun onlayn ariza.\n"
                                      f"📲contact : T.me/{message.contact.phone_number}")
                                      
    await bot.send_message(ADMINS[2], f"🙎🏻‍♂Mijoz : {ism}\n"
                                 f"🗂vazifa:🤝Shartnoma uchun onlayn ariza.\n"
                                      f"📲contact : T.me/{message.contact.phone_number}")
    await state.finish()