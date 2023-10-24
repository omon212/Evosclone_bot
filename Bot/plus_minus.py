
import logging
from aiogram import executor
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardRemove

from Keyboards.default import number_p, location, all_buttons, menu, menusetlarrr
from Keyboards.inline import comboqorachoy, fitcombooo

from bot import dp, Evos_state, bot, son

savatchamiz_user = {}


@dp.callback_query_handler(text='choy_plus',state=Evos_state.menu_setlar)
async def choy_plusss(call: types.CallbackQuery):
    global fake_son
    global son
    user_id = str(call.message.chat.id)
    fake_son = son.get(user_id, 0)
    fake_son += 1
    son[user_id] = fake_son
    if fake_son==0:
        await call.answer('0 dan ortga qaytib bolmaydi')


    await update_choy_plus(call.message.chat.id, call.message.message_id, fake_son)


async def update_choy_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='choy_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='choy_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='qorachoy_savat'),
            ],
        ],
    )

    # Edit the existing message to update the inline keyboard
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

@dp.callback_query_handler(text='choy_minus',state=Evos_state.menu_setlar)
async def choy_minus(call: types.CallbackQuery):
    global son
    global fake_son
    user_id = str(call.message.chat.id)
    fake_son = son.get(user_id, 0)
    fake_son -= 1
    son[user_id] = fake_son
    if fake_son==0:
        await call.answer('0 dan ortga qaytib bolmaydi')


    await update_choy_minus(call.message.chat.id, call.message.message_id, fake_son)


async def update_choy_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='choy_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='choy_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='qorachoy_savat'),
            ],
        ],
    )

    # Edit the existing message to update the inline keyboard
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)


@dp.callback_query_handler(text='qorachoy_savat')
async def qorasavet(call:types.CallbackQuery):
    savatchamiz_user[call.message.answer] = fake_son
    print(savatchamiz_user)












#-----------------Fitcombo-----------------#









@dp.callback_query_handler(text='fit_plus',state=Evos_state.menu_setlar)
async def fitcombo_plusss(call: types.CallbackQuery):
    global son

    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id, 0)
    fake_son += 1
    print(fake_son)
    son[user_id] = fake_son
    if fake_son==0:
        await call.answer('0 dan ortga qaytib bolmaydi')


    await update_fitcombo_plus(call.message.chat.id, call.message.message_id, fake_son)


async def update_fitcombo_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='fit_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='fit_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='fit_savat'),
            ],
        ],
    )

    # Edit the existing message to update the inline keyboard
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

@dp.callback_query_handler(text='fit_minus',state=Evos_state.menu_setlar)
async def fitcombo_minus(call: types.CallbackQuery):
    global son
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id, 0)
    fake_son -= 1
    print(fake_son)
    son[user_id] = fake_son
    if fake_son==0:
        await call.answer('0 dan ortga qaytib bolmaydi')
    else:
        user_id = str(call.message.chat.id)
        print(user_id)
        fake_son = son.get(user_id, 0)
        fake_son -= 1
        print(fake_son)
        son[user_id] = fake_son



    await update_fitcombo_minus(call.message.chat.id, call.message.message_id, fake_son)


async def update_fitcombo_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='fit_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='fit_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='fit_savat'),
            ],
        ],
    )

    # Edit the existing message to update the inline keyboard
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)


#-------------------------iftar-------------------------#





@dp.callback_query_handler(text='iftar_plus',state=Evos_state.menu_setlar)
async def fitcombo_plusss(call: types.CallbackQuery):
    global son

    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id, 0)
    fake_son += 1
    print(fake_son)
    son[user_id] = fake_son
    if fake_son==0:
        await call.answer('0 dan ortga qaytib bolmaydi')


    await update_iftar_plus(call.message.chat.id, call.message.message_id, fake_son)


async def update_iftar_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='iftar_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='iftar_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='iftar_savat'),
            ],
        ],
    )

    # Edit the existing message to update the inline keyboard
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

@dp.callback_query_handler(text='iftar_minus',state=Evos_state.menu_setlar)
async def fitcombo_minus(call: types.CallbackQuery):
    global son
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id, 0)
    fake_son -= 1
    print(fake_son)
    son[user_id] = fake_son
    if fake_son==0:
        await call.answer('0 dan ortga qaytib bolmaydi')
    else:
        user_id = str(call.message.chat.id)
        print(user_id)
        fake_son = son.get(user_id, 0)
        fake_son -= 1
        print(fake_son)
        son[user_id] = fake_son



    await update_iftar_minus(call.message.chat.id, call.message.message_id, fake_son)


async def update_iftar_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='iftar_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='iftar_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='iftar_savat'),
            ],
        ],
    )

    # Edit the existing message to update the inline keyboard
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)







#-----------------hotdog-+-------------#







@dp.callback_query_handler(text='hotdog_minus',state=Evos_state.menu_hotdog)
async def hotdog_minus(call: types.CallbackQuery):
    global son
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id, 0)
    fake_son -= 1
    print(fake_son)
    son[user_id] = fake_son




    await update_hotdog_minus(call.message.chat.id, call.message.message_id, fake_son)


async def update_hotdog_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='hotdog_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='hotdog_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='hotdog_savat'),
            ],
        ],
    )

    # Edit the existing message to update the inline keyboard
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

@dp.callback_query_handler(text='hotdog_plus',state=Evos_state.menu_hotdog)
async def hotdog_plus(call: types.CallbackQuery):
    global son
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id, 0)
    fake_son += 1
    print(fake_son)
    son[user_id] = fake_son



    await update_hotdog_plus(call.message.chat.id, call.message.message_id, fake_son)


async def update_hotdog_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='hotdog_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='hotdog_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='hotdog_savat'),
            ],
        ],
    )

    # Edit the existing message to update the inline keyboard
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)





#-----------------hotdog-+-------------#







@dp.callback_query_handler(text='ichimliklar_minus',state=Evos_state.menu_ichimliklar)
async def hotdog_minus(call: types.CallbackQuery):
    global son
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id, 0)
    fake_son -= 1
    print(fake_son)
    son[user_id] = fake_son




    await update_ichimliklar_minus(call.message.chat.id, call.message.message_id, fake_son)


async def update_ichimliklar_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='ichimliklar_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='ichimliklar_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='ichimliklar_savat'),
            ],
        ],
    )

    # Edit the existing message to update the inline keyboard
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

@dp.callback_query_handler(text='ichimliklar_plus',state=Evos_state.menu_ichimliklar)
async def hotdog_plus(call: types.CallbackQuery):
    global son
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id, 0)
    fake_son += 1
    print(fake_son)
    son[user_id] = fake_son



    await update_ichimliklar_plus(call.message.chat.id, call.message.message_id, fake_son)


async def update_ichimliklar_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='ichimliklar_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='ichimliklar_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='ichimliklar_savat'),
            ],
        ],
    )

    # Edit the existing message to update the inline keyboard
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)


