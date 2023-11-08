import logging
from aiogram import executor
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardRemove

from Keyboards.default import number_p, location, all_buttons, menu, menusetlarrr,buyurtma_berish
from Keyboards.inline import comboqorachoy, fitcombooo

from bot import dp, Evos_state, bot
from plus_minus import son
import sqlite3
#connect to savatcha.db
conn = sqlite3.connect('savatcha.db')
#cursor
c = conn.cursor()
#create table if not exists user_id and zakazlar
c.execute('''CREATE TABLE IF NOT EXISTS savatcha (
    user_id INTEGER,
    zakaz TEXT,
    narx INTEGER,
    son INTEGER
)''')

@dp.message_handler(text= "Savat 📥" )
async def savatcha(message: types.Message):
    global zakazlar
    c.execute(f"SELECT * FROM savatcha WHERE user_id = {message.chat.id}")
    zakazlar = c.fetchall()
    if zakazlar:
        for i in zakazlar:
            await message.answer(f'{i[1]} - {i[2]} so\'m - {i[3]} ta',reply_markup=buyurtma_berish)
    else:
        await message.answer('Savatcha bo\'sh')
    await Evos_state.buyurtma_berish.set()



@dp.callback_query_handler(text = 'qorachoy_savat')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[call.message.chat.id]} Savatga qo\'shildi')
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[call.message.chat.id]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000}")
        conn.commit()

    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Combo qora choy', {son[call.message.chat.id] * 16000}, {son[call.message.chat.id]})")
        conn.commit()





@dp.callback_query_handler(text = 'fit_savat')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son   )
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Fitcombo' AND narx = {son[str(call.message.chat.id)] * 30000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Fitcombo', {son[str(call.message.chat.id)] * 30000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()


@dp.callback_query_handler(text = 'iftarkoftegrill_savat')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son)
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Iftar kofte grill mol goshtidan' AND narx = {son[str(call.message.chat.id)] * 35000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Iftar kofte grill mol goshtidan', {son[str(call.message.chat.id)] * 35000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()


@dp.callback_query_handler(text = 'donarmol_savat')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son)
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Donar boks  mol goshtidan' AND narx = {son[str(call.message.chat.id)] * 34000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Donar boks  mol goshtidan', {son[str(call.message.chat.id)] * 34000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()

@dp.callback_query_handler(text = 'com_bo_savat')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son)
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'COMBO+' AND narx = {son[str(call.message.chat.id)] * 16000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'COMBO+', {son[str(call.message.chat.id)] * 16000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()


@dp.callback_query_handler(text = 'donarbokstovuq_savat')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son)
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Donar boks tovuq goshtidan' AND narx = {son[str(call.message.chat.id)] * 32000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Donar boks tovuq goshtidan', {son[str(call.message.chat.id)] * 32000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()

@dp.callback_query_handler(text = 'iftartovuqgosht_savat')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son)
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Iftar strips tovuq goshtidan' AND narx = {son[str(call.message.chat.id)] * 30000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Iftar strips tovuq goshtidan', {son[str(call.message.chat.id)] * 30000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()


@dp.callback_query_handler(text = 'kidscombo_savat')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son)
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Kids COMBO' AND narx = {son[str(call.message.chat.id)] * 16000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Kids COMBO', {son[str(call.message.chat.id)] * 16000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()


@dp.callback_query_handler(text = 'lavash2_savat')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son)
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Mol goshtidan qalampir lavash' AND narx = {son[str(call.message.chat.id)] * 26000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Mol goshtidan qalampir lavash', {son[str(call.message.chat.id)] * 26000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()


@dp.callback_query_handler(text = 'qalampirlavash_savat')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son)
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Tovuq goʼshtli qalampir lavash' AND narx = {son[str(call.message.chat.id)] * 24000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Tovuq goʼshtli qalampir lavash', {son[str(call.message.chat.id)] * 24000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()


@dp.callback_query_handler(text = 'mmolgoshtstandard_savat')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son)
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Mol goʼshtidan pishloqli lavash Standard' AND narx = {son[str(call.message.chat.id)] * 22000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Mol goʼshtidan pishloqli lavash Standard', {son[str(call.message.chat.id)] * 22000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()



@dp.callback_query_handler(text = 'standardcheese_plus')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son)
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Lavash cheese tovuq gosht Standart' AND narx = {son[str(call.message.chat.id)] * 27000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Lavash cheese tovuq gosht Standart', {son[str(call.message.chat.id)] * 27000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()

@dp.callback_query_handler(text = 'fitter_savat')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son)
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'FITTER' AND narx = {son[str(call.message.chat.id)] * 22000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'FITTER', {son[str(call.message.chat.id)] * 22000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()


@dp.callback_query_handler(text = 'tovuqgosht_savat')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son)
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Lavash tovuq gosht' AND narx = {son[str(call.message.chat.id)] * 22000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Lavash tovuq gosht', {son[str(call.message.chat.id)] * 22000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()


#-----------shaurma----------#


@dp.callback_query_handler(text = 'shaurmatovuqg_savat')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son)
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Shaurma tovuq gosht' AND narx = {son[str(call.message.chat.id)] * 24000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Shaurma tovuq gosht', {son[str(call.message.chat.id)] * 24000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()


@dp.callback_query_handler(text = 'qmolgosht_savat')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son)
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Shaurma qalampir mol gosht' AND narx = {son[str(call.message.chat.id)] * 22000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Shaurma qalampir mol gosht', {son[str(call.message.chat.id)] * 22000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()

@dp.callback_query_handler(text = 'shmolgosht_savat')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son)
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Shaurma mol gosht' AND narx = {son[str(call.message.chat.id)] * 24000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Shaurma mol gosht', {son[str(call.message.chat.id)] * 24000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()


@dp.callback_query_handler(text = 'gamburger_savat')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son)
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Gamburger' AND narx = {son[str(call.message.chat.id)] * 22000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Gamburgere', {son[str(call.message.chat.id)] * 22000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()

@dp.callback_query_handler(text = 'doubleburgere_savat')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son)
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Double burger' AND narx = {son[str(call.message.chat.id)] * 33000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Double burger', {son[str(call.message.chat.id)] * 33000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()


@dp.callback_query_handler(text = 'doublecheese_savat')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son)
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Double cheese' AND narx = {son[str(call.message.chat.id)] * 37000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Double cheese', {son[str(call.message.chat.id)] * 37000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()

@dp.callback_query_handler(text = 'cheeseburger_savat')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son)
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Cheeseburger' AND narx = {son[str(call.message.chat.id)] *24000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Cheeseburger', {son[str(call.message.chat.id)] *24000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()




#------------------hotdog-------------------#

@dp.callback_query_handler(text = 'hotdogbagguate_savat')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son)
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Hot-dog bagguate' AND narx = {son[str(call.message.chat.id)] *14000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Hot-dog bagguate', {son[str(call.message.chat.id)] *14000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()

@dp.callback_query_handler(text = 'subtovuqcheese_savat')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son)
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Sub tovuq cheese' AND narx = {son[str(call.message.chat.id)] *19000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Sub tovuq cheese', {son[str(call.message.chat.id)] *19000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()



@dp.callback_query_handler(text = 'subtovuq_savat')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son)
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Sub tovuq' AND narx = {son[str(call.message.chat.id)] *17000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Sub tovuq', {son[str(call.message.chat.id)] *17000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()


@dp.callback_query_handler(text = 'hotdogbagguated_savat')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son)
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Hot-dog baguette double' AND narx = {son[str(call.message.chat.id)] *21000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Hot-dog baguette double', {son[str(call.message.chat.id)] *21000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()


@dp.callback_query_handler(text = 'hotdogkids_savat')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son)
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Hot-dog kids' AND narx = {son[str(call.message.chat.id)] *8000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Hot-dog kids', {son[str(call.message.chat.id)] *8000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()



@dp.callback_query_handler(text = 'subgoshtcheese_savat')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son)
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Sub gosht cheese' AND narx = {son[str(call.message.chat.id)] *21000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Sub gosht cheese', {son[str(call.message.chat.id)] *21000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()


@dp.callback_query_handler(text = 'hotdogclasic_savat')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son)
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Hot-dog classic' AND narx = {son[str(call.message.chat.id)] *8000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Hot-dog classic', {son[str(call.message.chat.id)] *8000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()


@dp.callback_query_handler(text = 'subgosht_minus')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son)
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Subgosht' AND narx = {son[str(call.message.chat.id)] *8000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Subgosht', {son[str(call.message.chat.id)] *8000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()


#-----------ichimliklar---------#
@dp.callback_query_handler(text='sokdena_savat')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son)
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Sok dena 0,33l' AND narx = {son[str(call.message.chat.id)] * 10000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Sok dena 0,33l', {son[str(call.message.chat.id)] * 10000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()


@dp.callback_query_handler(text='suv05_savat')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son)
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Suv 0,5' AND narx = {son[str(call.message.chat.id)] * 4000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Suv 0,5', {son[str(call.message.chat.id)] * 4000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()


@dp.callback_query_handler(text='pepsi05_savat')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son)
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Pepsi 0,5' AND narx = {son[str(call.message.chat.id)] * 9000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Pepsi 0,5', {son[str(call.message.chat.id)] * 9000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()

@dp.callback_query_handler(text='pepsi15_savat')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son)
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Pepsi 1,5' AND narx = {son[str(call.message.chat.id)] * 17000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Pepsi 1,5', {son[str(call.message.chat.id)] * 17000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()


@dp.callback_query_handler(text='quyibpepsi_savat')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son)
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Quyib beriladigan Pepsi' AND narx = {son[str(call.message.chat.id)] * 8000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Quyib beriladigan Pepsi', {son[str(call.message.chat.id)] * 8000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()


@dp.callback_query_handler(text='blisharbat_savat')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son)
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Bliss sharbati' AND narx = {son[str(call.message.chat.id)] * 16000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Bliss sharbati', {son[str(call.message.chat.id)] * 16000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()


@dp.callback_query_handler(text='Amerikano_savat')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son)
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Amerikano' AND narx = {son[str(call.message.chat.id)] * 11000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Amerikano', {son[str(call.message.chat.id)] * 11000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()

@dp.callback_query_handler(text='lattle_savat')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son)
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Latte' AND narx = {son[str(call.message.chat.id)] * 13000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Latte', {son[str(call.message.chat.id)] * 13000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()

@dp.callback_query_handler(text='kokchoy_savat')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son)
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Kok choy' AND narx = {son[str(call.message.chat.id)] * 4000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Kok choy', {son[str(call.message.chat.id)] * 4000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()


@dp.callback_query_handler(text='qorachoyo_savat')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son)
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Qora choy' AND narx = {son[str(call.message.chat.id)] * 4000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Qora choy', {son[str(call.message.chat.id)] * 4000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()


@dp.callback_query_handler(text='asalim_savat')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son)
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Medovik Asalim' AND narx = {son[str(call.message.chat.id)] * 16000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Medovik Asalim', {son[str(call.message.chat.id)] * 16000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()


@dp.callback_query_handler(text='chizkeyk_savat')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son)
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Chizkeyk' AND narx = {son[str(call.message.chat.id)] * 16000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Chizkeyk', {son[str(call.message.chat.id)] * 16000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()


@dp.callback_query_handler(text='karamelin_savat')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son)
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Donut karameli' AND narx = {son[str(call.message.chat.id)] * 15000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Donut karameli', {son[str(call.message.chat.id)] * 15000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()

@dp.callback_query_handler(text='mevali_savat')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son)
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Donut mevali' AND narx = {son[str(call.message.chat.id)] * 15000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Donut mevali', {son[str(call.message.chat.id)] * 15000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()


@dp.callback_query_handler(text='ketchup_savat')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son)
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Ketchup' AND narx = {son[str(call.message.chat.id)] * 2000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Ketchup', {son[str(call.message.chat.id)] * 2000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()

@dp.callback_query_handler(text='guruch_savat')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son)
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Guruch' AND narx = {son[str(call.message.chat.id)] * 7000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Guruch', {son[str(call.message.chat.id)] * 7000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()


@dp.callback_query_handler(text='tovuqstrips_savat')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son)
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Tovuq Strips' AND narx = {son[str(call.message.chat.id)] * 19000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Tovuq Strips', {son[str(call.message.chat.id)] * 19000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()


@dp.callback_query_handler(text='pishloqli_sous_savat')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son)
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Pishloqli sous' AND narx = {son[str(call.message.chat.id)] * 2000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Pishloqli sous', {son[str(call.message.chat.id)] * 2000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()


@dp.callback_query_handler(text='chisnokli_sous_savat')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son)
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Chisnokli sous' AND narx = {son[str(call.message.chat.id)] * 2000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Chisnokli sous', {son[str(call.message.chat.id)] * 2000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()


@dp.callback_query_handler(text='chilisous_savat')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son)
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Chisnokli sous' AND narx = {son[str(call.message.chat.id)] * 2000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Chisnokli sous', {son[str(call.message.chat.id)] * 2000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()

@dp.callback_query_handler(text='barbekusous_savat')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son)
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Barbekyu sousi' AND narx = {son[str(call.message.chat.id)] * 2000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Barbekyu sousi', {son[str(call.message.chat.id)] * 2000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()


@dp.callback_query_handler(text='salat_savat')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son)
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Salat' AND narx = {son[str(call.message.chat.id)] * 7000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Salat', {son[str(call.message.chat.id)] * 7000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()

@dp.callback_query_handler(text='non_savat')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son)
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Non' AND narx = {son[str(call.message.chat.id)] * 3000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Non', {son[str(call.message.chat.id)] * 3000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()


@dp.callback_query_handler(text='fri_savat')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son)
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Fri' AND narx = {son[str(call.message.chat.id)] * 14000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Fri', {son[str(call.message.chat.id)] * 14000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()

@dp.callback_query_handler(text='qtovuqgosht_savat')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son)
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Shaurma qalampir tovuq gosht' AND narx = {son[str(call.message.chat.id)] * 26000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Shaurma qalampir tovuq gosht', {son[str(call.message.chat.id)] * 26000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()



@dp.callback_query_handler(text='subgosht_savat')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son)
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Sub gosht' AND narx = {son[str(call.message.chat.id)] * 19000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Sub gosht', {son[str(call.message.chat.id)] * 19000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()



@dp.callback_query_handler(text='limonchoy_savat')
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[str(call.message.chat.id)]} Savatga qo\'shildi')
    print(son)
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[str(call.message.chat.id)]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Limonli kok choy' AND narx = {son[str(call.message.chat.id)] * 5000}")
        conn.commit()
        conn.close()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Limonli kok choy', {son[str(call.message.chat.id)] * 5000}, {son[str(call.message.chat.id)]})")
        conn.commit()
        conn.close()