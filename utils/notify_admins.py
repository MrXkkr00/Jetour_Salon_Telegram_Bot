import logging

from aiogram import Dispatcher

from data.config import ADMINS
from keyboards.default.bosh_nemu import bosh_menu


async def on_startup_notify(dp: Dispatcher):
        try:
            await dp.bot.send_message(ADMINS[0], "Bot ishga tushdi", reply_markup=bosh_menu)

        except Exception as err:
            logging.exception(err)
