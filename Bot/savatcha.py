import logging
from aiogram import executor
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardRemove

from Keyboards.default import number_p, location, all_buttons, menu, menusetlarrr
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
    c.execute(f"SELECT * FROM savatcha WHERE user_id = {message.chat.id}")
    zakazlar = c.fetchall()
    if zakazlar:
        for i in zakazlar:
            await message.answer(f'{i[1]} - {i[2]} so\'m - {i[3]} ta')
    else:
        await message.answer('Savatcha bo\'sh')



@dp.callback_query_handler(text = 'qorachoy_savat',state=Evos_state.menu_setlar)
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


@dp.callback_query_handler(text = 'fit_savat',state=Evos_state.menu_setlar)
async def savatcha(call: types.CallbackQuery):
    await call.message.delete()
    print(son)
    await call.message.answer(f'+{son[call.message.chat.id]} Savatga qo\'shildi')
    # await c.execute(
    #     f"SELECT * FROM savatcha WHERE user_id = {call.message.chat.id} AND zakaz = 'Combo qora choy' AND narx = {son[call.message.chat.id] * 16000} AND son = {son[call.message.chat.id]}")
    zakazlar = c.fetchall()
    if zakazlar:
        await c.execute(
            f"UPDATE savatcha SET son = {son[call.message.chat.id]} WHERE user_id = {call.message.chat.id} AND zakaz = 'Fitcombo' AND narx = {son[call.message.chat.id] * 16000}")
        conn.commit()
    else:
        await c.execute(
            f"INSERT INTO savatcha VALUES ({call.message.chat.id}, 'Fitcombo', {son[call.message.chat.id] * 16000}, {son[call.message.chat.id]})")
        conn.commit()


