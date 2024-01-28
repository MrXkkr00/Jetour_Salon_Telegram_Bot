import sqlite3

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.default.bosh_nemu import bosh_menu
from data.config import ADMINS


class Database:
    def __init__(self, path_to_db="./data/reklama.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users_rek(self):
        sql = """
        CREATE TABLE Users_rek (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id int NOT NULL,
            name varchar(150)
            );
"""
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user_rek(self, user_id, name: str = None):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Users_rek( user_id, name ) VALUES(?, ?)
        """
        self.execute(sql, parameters=(user_id, name), commit=True)

    def select_all_users_rek(self):
        sql = """
        SELECT * FROM Users_rek
        """
        return self.execute(sql, fetchall=True)

    def select_user_rek(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM Users_rek WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_users_rek(self):
        return self.execute("SELECT COUNT(*) FROM Users_rek;", fetchone=True)

    def delete_users_rek(self):
        self.execute("DELETE FROM Users_rek WHERE TRUE", commit=True)


def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")



from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, bot

db = Database(path_to_db="./data/reklama.db")


@dp.message_handler(text="/start")
async def bot_s1213tart(message: types.Message):
    try:
        db.create_table_users_rek()
    except:
        pass
    user_id = message.from_user.id
    user = db.select_user_rek(user_id=user_id)
    if not user:
        db.add_user_rek(user_id=user_id, name=message.from_user.username)
        f = open("./data/reklama.txt", "a")
        f.write(f"{user_id}\n")
        f.close()
    await message.answer(f"Assalomu Alaykum, {message.from_user.full_name}!\nBotimizga hush kelibsiz",
                         reply_markup=bosh_menu)


class Reklama_State(StatesGroup):
    text = State()


@dp.message_handler(text_contains="//rek")
async def bot2342_start(message: types.Message, state: FSMContext):
    msg = message.text[5:]
    # sum = str(db.count_users_rek())
    # sum = int(sum[1:-2])
    # for i in range(sum):
    #     user = db.select_user_rek(id=i + 1)
    #     await bot.send_message(user[1], msg)
    await state.update_data(
        {"msg": msg}
    )

    await message.answer(f"Rasm yuboring")
    await Reklama_State.text.set()


@dp.message_handler(content_types=["photo"], state=Reklama_State.text)
async def bot_text(message: types.Message, state: FSMContext):
    document_id = message.photo[0].file_id
    file_info = await bot.get_file(document_id)
    data = await state.get_data()
    msg = data.get("msg")
    sum = str(db.count_users_rek())
    sum = int(sum[1:-2])
    for i in range(sum):
        user = db.select_user_rek(id=i + 1)
        await bot.send_photo(chat_id=user[1], photo=file_info.file_id, caption=msg)
    await state.finish()


@dp.message_handler(text="//count")
async def bot22_start(message: types.Message):
    sum = str(db.count_users_rek())
    sum = int(sum[1:-2])
    await message.answer(f"{sum}")


@dp.message_handler(text="//all")
async def bot22_start(message: types.Message):
    sum = str(db.count_users_rek())
    sum = int(sum[1:-2])
    for i in range(sum):
        user = db.select_user_rek(id=i + 1)
        await bot.send_message(ADMINS[0], f"{user[0]}    {user[1]}   @{user[2]}")

# @dp.message_handler(commands=['photo'])
# async def process_photo_command(message: types.Message):
#     caption = 'Какие глазки! :eyes:'
#     await bot.send_photo(message.from_user.id, CAT_BIG_EYES,
#                          caption=emojize(caption),
#                          reply_to_message_id=message.message_id)
