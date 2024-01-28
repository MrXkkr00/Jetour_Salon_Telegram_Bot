from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import InputFile

from keyboards.default.bosh_nemu import bosh_menu, bosh_menu_ru, modellar_uz_ru
from loader import dp, bot


@dp.message_handler(text="📍Manzil")
async def bot_start(message: types.Message):
    lat = 41.206294
    lon = 69.221745
    # reply = "latitude:  {}\nlongitude: {}".format(lat, lon)
    await bot.send_location(message.from_user.id, lat, lon)
    await message.answer(text=f"Sergeli 2-mavze 5-metro bekat 'Jetour' avtosaloni", reply_markup=bosh_menu)



@dp.message_handler(text="🏠 Asosiy menu")
async def bot_s23rt(message: types.Message):
    await message.answer(f"Assalomu Alaykum, {message.from_user.full_name}!\nBotimizga hush kelibsiz",
                         reply_markup=bosh_menu)







@dp.message_handler(text="🇺🇿🔄")
async def bot_s56rt(message: types.Message):
    await message.answer(f"Assalomu Alaykum, {message.from_user.full_name}!\nBotimizga hush kelibsiz",
                         reply_markup=bosh_menu)


@dp.message_handler(text="💵 Narxlar jadvali")
async def bot_s14rt(message: types.Message):
    # await bot.send_location(message.from_user.id, InputFile("Цены.xls"))
    await message.answer_document(InputFile("./data/Narxlar.xls"))


@dp.message_handler(text="☎️ Biz bilan aloqa")
async def bot_s78t(message: types.Message):
    await message.answer(f"Aloqa uchun raqamlarimiz\n78 113 03 00\n91 033 30 03 \n"
                         f"99 305 03 30 \n77 041 30 03\n77 042 30 03")


@dp.message_handler(text="🏎Avtomobillarimiz haqida ma'lumotlar")
async def bot_st98rt(message: types.Message):
    await message.answer(f"Model turini tanlang",
                         reply_markup=modellar_uz_ru)


@dp.message_handler(text="JETOUR")
async def bot_st15t(message: types.Message):
    await message.answer_document(InputFile("./data/Jetour/X90plus.pdf"), caption="1.6 TURBO 197 HP	💵 436.250.000 so'm"
                                                                                  "\n2.0 TURBO 254 HP	💵 461.250.000 so'm")
    await message.answer_document(InputFile("./data/Jetour/X70plus.pdf"),
                                  caption="1.6 L TURBO 197 HP	💵 393.750.000 so'm"
                                          "\n1.5 L TURBO 156 HP	💵 348.750.000 so'm")
    await message.answer_document(InputFile("./data/Jetour/X70.pdf"), caption="1.5 L TURBO 148 HP	💵 317.500.000 so'm\n"
                                                                              "'STANDART PAKET' 💵 296.250.000 so'm")
    await message.answer_document(InputFile("./data/Jetour/Dashing.pdf"),               caption=f"CONFORT PAKET	1.5L TURBO 156 HP 💵 331 250 000 so'm"
                          f"FULL PAKET 	1.6L TURBO 197 HP 💵 373 750 000 so'm")


@dp.message_handler(text="HONGQI")
async def bot21start(message: types.Message):
    await message.answer_document(InputFile(f"./data/Hongqi/Hongqi E-QM5.pdf"),
                                  caption="STANDART PAKET	💵 287.500.000 so'm\n")
    await message.answer_document(InputFile(f"./data/Hongqi/Hongqi E-HS9.pdf"), caption="💵 1.250.000.000 so'm")
    await message.answer_document(InputFile(f"./data/Hongqi/Hongqi H9.pdf"), caption="💵 1.125.000.000 so'm")
    await message.answer_document(InputFile(f"./data/Hongqi/Hongqi H5.pdf"),
                                  caption="1.8 TURBO 197 HP	💵 373.750.000 so'm\n"
                                          "'STANDART  PAKET' 💵 350.000.000 so'm")
    await message.answer_document(InputFile(f"./data/Hongqi/Hongqi Hs5.pdf"),
                                  caption="AWD 2 L T 224 HP 	💵 525.000.000 so'm\n"
                                          "FWD 2 L T 224 HP 	💵 475.000.000 so'm\n")


@dp.message_handler(text="BESTUNE")
async def bot_st613art(message: types.Message):
    await message.answer_document(InputFile(f"./data/Bestune/Bestune T55.pdf"),
                                  caption="1.5 L Turbo 169 HP	💵 311.250.000 so'm\n"
                                          "STANDART  PAKET	💵 287.500.000 so'm\n")
    await message.answer_document(InputFile(f"./data/Bestune/Bestune T99.pdf"),
                                  caption="2 L Turbo 224 HP 	💵 500.000.000 so'm\n"
                                          "'STANDARD  PAKET' 💵 450.000.000 so'm\n")


@dp.message_handler(text="DONGFENG")
async def bot_sta14314rt(message: types.Message):
    await message.answer_document(InputFile(f"data/Dongfeng/Aeolus Huge.pdf"),
                                  caption="1.5 L TURBO   💵 412.500.000 so'm\n"
                                          "177  HP  HEV  💵 375.000.000 so'm\n")
    await message.answer_document(InputFile(f"./data/Dongfeng/Aeolus A60 Max HEV.pdf"),
                                  caption="1.5 L TURBO 190 HP	💵 350.000.000 so'm\n"
                                          "HYBRID  1.5 L TURBO  💵	375.000.000 so'm")
    await message.answer_document(InputFile(f"data/Dongfeng/Forthing T5 evo.pdf"),
                                  caption="HYBRID	💵 375.000.000 so'm\n"
                                          "1.5 L TURBO 197 HP	💵 350.000.000 so'm\n")
    await message.answer_document(InputFile(f"data/Dongfeng/Fengon S508 evr.pdf"),
                                  caption="177 HP + ELECTRIC ENGINE POWER	💵 381.250.000 so'm")
    await message.answer_document(InputFile(f"data/Dongfeng/Fengon 580.pdf"))
    await message.answer_document(InputFile(f"data/Dongfeng/Aeolus Shine.pdf"),
                                  caption="1.5 L TURBO 190 HP	💵 287.500.000 so'm\n"
                                          "1.5 L ATMOSFERA FULL PAKET 💵 248.750.000 so'm\n"
                                          "1.5 L ATMOSFERA STANDART PAKET 💵 236.250.000 so'm\n")


@dp.message_handler(text="AIQAR")
async def bot_78686start(message: types.Message):
    await message.answer_document(InputFile(f"data/Aiqar/Aiqar Eq7.pdf"), 
                                  caption = f"BATTARY 66 KW/H 211 HP 512 KM"
                                  f"\n 💵 374.375.000so'm\n")

@dp.message_handler(text="SHINERAY")
async def bot_st8686art(message: types.Message):
    await message.answer_document(InputFile("./data/Shineray/Shineray_price.xls"))




@dp.message_handler(text="🏢 Kompaniyamiz haqida")
async def bot_stk5666kart(message: types.Message):
    await message.answer(f"Jetour kompaniyasi 1997-yilda tashkil qilingan hoding kompaniya negizida 2018-yilda tashkil"
                         f" topgan. Asosiy faoliyati sayohatga mo’ljallangan oilaviy krossoverlar ishlab chiqarish hisoblanadi."
                         f" Brendning xitoycha nomi 'Jietu' deb talaffuz qilinadi va o’zbek tiliga eng yaxshi tarjimasi "
                         f"bu 'G'alaba yo'li' ma’nosini anglatadi. Jetourning butun mahsulot assortimenti 5, 6 yoki 7 "
                         f"o‘rinli konfiguratsiya variantlari bilan o‘rta segment uchun mo’ljallangan , shu bilan birga "
                         f"ichki yonuv dvigatelli, to‘liq elektr, plagin-gibrid va kelajakda vodorodli avtomobillar ham "
                         f"ishlab chiqarishni ko’zda tutadi. 2018- yilning yanvar oyida Pekindagi avtoko’rgazmada Jetour"
                         f" X70S oilaviy SUV ni va Jetour X nomli konsep avtomobillarini taqdim etdi. O’sha yilning "
                         f"o’zidayoq X70 oylik sotuvlarini 10.000 donadan oshirishga erishgan. 2019-yilda muvaffaqiyatli "
                         f"tarzda sotuvlar esa 134.000 donadan oshadi va shu tariqa Jetour katta bozorlarga yuqari tezlikda"
                         f" krishga erishgan. Jetourning umumiy savdo hajmi 300 000 donadan oshdi va 28 oy ichida 300 000 "
                         f"sotuv hajmiga erishgan birinchi Xitoy brendiga aylandi.2022 yilning iyuligacha Jetour dunyoning "
                         f"30 dan ortiq mamlakatlariga kirdi va 700 millionga yaqin xaridorga ega bo’ldi. Jetour rasmiy "
                         f"dillerlik tarmog'ining umumiy soni 300 dan oshdi va 2025 yil oxiriga kelib 1500 taga etishi "
                         f"kutilayabdi. Hozirgi paytda kompaniya tarkibida X90 PLUS , Shanhai L9, Traveller ,X70 PLUS, "
                         f"X70, Dashing kabi o’nlab modellarni taqdim etib ulgurdi. Brend nomi inglizcha JET (jet) va "
                         f"TOUR (sayohat) so‘zlarining birikmasi ma'nolarini ham ifodalay oladi. Bu avtomobilda sayohat "
                         f"qilish shaxsiy samolyotda uchish kabi rohatbag'ishlashi va nihoyatda qulay bo‘lishi "
                         f"mumkinligini anglatadi.Brend turli sohalarda tinmay mehnat qiladigan va oxir-oqibat o‘z "
                         f"maqsadlariga erishadigan, yangi ufqlarni ochadigan, baxtli uyg‘un hayot izlovchilar uchun "
                         f"mo‘ljallangan.")
