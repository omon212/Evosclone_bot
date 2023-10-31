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


@dp.callback_query_handler(text='choy_plus')
async def choy_plusss(call: types.CallbackQuery):
    global fake_son
    user_id = call.message.chat.id
    fake_son = son.get(user_id, 0)
    fake_son += 1
    son[user_id] = fake_son
    if fake_son == 0:
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


@dp.callback_query_handler(text='choy_minus')
async def choy_minus(call: types.CallbackQuery):
    global fake_son
    user_id = call.message.chat.id
    fake_son = son.get(user_id, 0)
    fake_son -= 1
    son[user_id] = fake_son
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


# -----------------Fitcombo-----------------#


@dp.callback_query_handler(text='fit_plus')
async def fitcombo_plusss(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id, 0)
    fake_son += 1
    print(fake_son)
    son[user_id] = fake_son
    if fake_son == 0:
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


@dp.callback_query_handler(text='fit_minus')
async def fitcombo_minus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id, 0)
    fake_son += 1
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


# -------------------------iftar-------------------------#


@dp.callback_query_handler(text='iftar_plus')
async def fitcombo_plusss(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id, 0)
    fake_son += 1
    print(fake_son)
    son[user_id] = fake_son

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


@dp.callback_query_handler(text='iftar_minus')
async def fitcombo_minus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id, 0)
    fake_son += 1
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


# -------------------donarboks-------------------#


@dp.callback_query_handler(text='donarboks_plus')
async def fitcombo_plusss(call: types.CallbackQuery):
    son[call.message.from_user.id] = 1
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id, 0)
    fake_son += 1
    print(fake_son)
    son[user_id] = fake_son

    await update_donarboks_plus(call.message.chat.id, call.message.message_id, fake_son)


async def update_donarboks_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='donarboks_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='donarboks_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='donarboks_savat'),
            ],
        ],
    )

    # Edit the existing message to update the inline keyboard
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)





@dp.callback_query_handler(text='donarboks_minus')
async def fitcombo_plusss(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id, 0)
    fake_son -= 1
    print(fake_son)
    son[user_id] = fake_son

    await update_donarboks_minus(call.message.chat.id, call.message.message_id, fake_son)


async def update_donarboks_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='donarboks_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='donarboks_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='donarboks_savat'),
            ],
        ],
    )

    # Edit the existing message to update the inline keyboard
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)





# -------------------donarbokstovuqgosht-------------------#


@dp.callback_query_handler(text='donarboks_plus')
async def fitcombo_plusss(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id, 0)
    fake_son += 1
    print(fake_son)
    son[user_id] = fake_son

    await update_donarboks_plus(call.message.chat.id, call.message.message_id, fake_son)


async def update_donarboks_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='donarboks_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='donarboks_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='donarboks_savat'),
            ],
        ],
    )

    # Edit the existing message to update the inline keyboard
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)





@dp.callback_query_handler(text='donarboks_minus')
async def fitcombo_plusss(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id, 0)
    fake_son -= 1
    print(fake_son)
    son[user_id] = fake_son

    await update_donarboks_minus(call.message.chat.id, call.message.message_id, fake_son)


async def update_donarboks_minus(chat_id, message_id, new_son):
        new_buttons = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton('➖', callback_data='donarboks_minus'),
                    InlineKeyboardButton(f"{new_son}", callback_data='son'),
                    InlineKeyboardButton('➕', callback_data='donarboks_plus')
                ],
                [
                    InlineKeyboardButton("Savatga qo'shish", callback_data='donarboks_savat'),
                ],
            ],
        )

        # Edit the existing message to update the inline keyboard
        await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)



#-------------------combo-------------------#

@dp.callback_query_handler(text='com_bo_plus')
async def combo_plusss(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id, 0)
    fake_son += 1
    print(fake_son)
    son[user_id] = fake_son

    await update_co_mbo_plus(call.message.chat.id, call.message.message_id, fake_son)

async def update_co_mbo_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='com_bo_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='com_bo_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='com_bo_savat'),
            ],
        ],
    )

    # Edit the existing message to update the inline keyboard
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

@dp.callback_query_handler(text='com_bo_minus')
async def combo_plusss(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id, 0)
    fake_son -= 1
    print(fake_son)
    son[user_id] = fake_son

    await update_co_mbo_plus(call.message.chat.id, call.message.message_id, fake_son)

async def update_co_mbo_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='com_bo_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='com_bo_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='com_bo_savat'),
            ],
        ],
    )

    # Edit the existing message to update the inline keyboard
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)



#-------------------combotovuqgosht-------------------#

@dp.callback_query_handler(text='donarbokstovuq_minus')
async def combo_plusss(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id, 0)
    fake_son -= 1
    print(fake_son)
    son[user_id] = fake_son

    await update_donarbokstovuq_minus(call.message.chat.id, call.message.message_id, fake_son)

async def update_donarbokstovuq_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='donarbokstovuq_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='donarbokstovuq_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='donarbokstovuq_savat'),
            ],
        ],
    )

    # Edit the existing message to update the inline keyboard
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

@dp.callback_query_handler(text='donarbokstovuq_plus')
async def combo_plusss(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id, 0)
    fake_son += 1
    print(fake_son)
    son[user_id] = fake_son

    await update_donarbokstovuq_plus(call.message.chat.id, call.message.message_id, fake_son)

async def update_donarbokstovuq_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='donarbokstovuq_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='donarbokstovuq_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='donarbokstovuq_savat'),
            ],
        ],
    )

    # Edit the existing message to update the inline keyboard
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

#-------------------iftartovuqgosht-------------------#

@dp.callback_query_handler(text='iftartovuqgosht_minus')
async def combo_plusss(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id, 0)
    fake_son -= 1
    print(fake_son)
    son[user_id] = fake_son

    await update_iftartovuqgosht_minus(call.message.chat.id, call.message.message_id, fake_son)

async def update_iftartovuqgosht_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='iftartovuqgosht_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='iftartovuqgosht_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='iftartovuqgosht_savat'),
            ],
        ],
    )

    # Edit the existing message to update the inline keyboard
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

@dp.callback_query_handler(text='iftartovuqgosht_plus')
async def combo_plusss(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id, 0)
    fake_son += 1
    print(fake_son)
    son[user_id] = fake_son

    await update_iftartovuqgosht_plus(call.message.chat.id, call.message.message_id, fake_son)

async def update_iftartovuqgosht_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='iftartovuqgosht_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='iftartovuqgosht_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='iftartovuqgosht_savat'),
            ],
        ],
    )

    # Edit the existing message to update the inline keyboard
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

#-------------------kidscombo-------------------#

@dp.callback_query_handler(text='kidscombo_minus')
async def combo_plusss(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id, 0)
    fake_son -= 1
    print(fake_son)
    son[user_id] = fake_son

    await update_kidscombo_minus(call.message.chat.id, call.message.message_id, fake_son)

async def update_kidscombo_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='kidscombo_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='kidscombo_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='kidscombo_savat'),
            ],
        ],
    )

    # Edit the existing message to update the inline keyboard
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

@dp.callback_query_handler(text='kidscombo_plus')
async def combo_plusss(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id, 0)
    fake_son += 1
    print(fake_son)
    son[user_id] = fake_son

    await update_kidscombo_plus(call.message.chat.id, call.message.message_id, fake_son)

async def update_kidscombo_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='kidscombo_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='kidscombo_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='kidscombo_savat'),
            ],
        ],
    )

    # Edit the existing message to update the inline keyboard
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

#-------------------iftarkoftegrill-------------------#

@dp.callback_query_handler(text='iftarkoftegrill_minus')
async def combo_plusss(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id, 0)
    fake_son -= 1
    print(fake_son)
    son[user_id] = fake_son

    await update_iftarkoftegrill_minus(call.message.chat.id, call.message.message_id, fake_son)

async def update_iftarkoftegrill_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='iftarkoftegrill_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='iftarkoftegrill_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='iftarkoftegrill_savat'),
            ],
        ],
    )

    # Edit the existing message to update the inline keyboard
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

@dp.callback_query_handler(text='iftarkoftegrill_plus')
async def combo_plusss(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id, 0)
    fake_son += 1
    print(fake_son)
    son[user_id] = fake_son

    await update_iftarkoftegrill_plus(call.message.chat.id, call.message.message_id, fake_son)

async def update_iftarkoftegrill_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='iftarkoftegrill_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='iftarkoftegrill_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='iftarkoftegrill_savat'),
            ],
        ],
    )

    # Edit the existing message to update the inline keyboard
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

#-------------------donarmol-------------------#

@dp.callback_query_handler(text='donarmol_minus')
async def donarmol_minus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id, 0)
    fake_son -= 1
    print(fake_son)
    son[user_id] = fake_son

    await update_donarmol_minus(call.message.chat.id, call.message.message_id, fake_son)

async def update_donarmol_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='donarmol_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='donarmol_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='donarmol_savat'),
            ],
        ],
    )

    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

@dp.callback_query_handler(text='donarmol_plus')
async def donarmol_plus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id, 0)
    fake_son += 1
    print(fake_son)
    son[user_id] = fake_son
    await update_donarmol_plus(call.message.chat.id, call.message.message_id, fake_son)

async def update_donarmol_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='donarmol_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='donarmol_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='donarmol_savat'),
            ],
        ],
    )

    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

#-------------------lavash2-------------------#

@dp.callback_query_handler(text='lavash2_minus')
async def lavash2_minus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id, 0)
    print(fake_son)
    fake_son -= 1
    son[user_id] = fake_son
    await update_lavash2_minus(call.message.chat.id, call.message.message_id, fake_son)

async def update_lavash2_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='lavash2_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='lavash2_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='lavash2_savat'),
            ],
        ],
    )

    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

@dp.callback_query_handler(text='lavash2_plus')
async def lavash2_plus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id, 0)
    print(fake_son)
    fake_son += 1
    son[user_id] = fake_son
    await update_lavash2_plus(call.message.chat.id, call.message.message_id, fake_son)

async def update_lavash2_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='lavash2_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='lavash2_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='lavash2_savat'),
            ],
        ],
    )

    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)


#-------------------lavash2-------------------#
@dp.callback_query_handler(text='lavash2_minus')
async def lavash_minus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id, 1)
    print(fake_son)
    fake_son -= 1
    son[user_id] = fake_son
    await update_lavash_minus(call.message.chat.id, call.message.message_id, fake_son)

async def update_lavash_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='lavash2_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='lavash2_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='lavash2_savat'),
            ],
        ],
    )

    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)



@dp.callback_query_handler(text='lavash2_plus')
async def lavash_plus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id, 1)
    print(fake_son)
    fake_son += 1
    son[user_id] = fake_son
    await update_lavash_plus(call.message.chat.id, call.message.message_id, fake_son)

async def update_lavash_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='lavash2_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='lavash2_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='lavash2_savat'),
            ],
        ],
    )

    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

#-------------------qalampirlavash-------------------#
@dp.callback_query_handler(text='qalampirlavash_minus')
async def qalampirlavash_minus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id, 1)
    print(fake_son)
    fake_son -= 1
    son[user_id] = fake_son
    await update_qalampirlavash_minus(call.message.chat.id, call.message.message_id, fake_son)

async def update_qalampirlavash_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='qalampirlavash_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='qalampirlavash_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='qalampirlavash_savat'),
            ],
        ],
    )

    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

@dp.callback_query_handler(text='qalampirlavash_plus')
async def qalampirlavash_plus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id, 1)
    print(fake_son)
    fake_son += 1
    son[user_id] = fake_son
    await update_qalampirlavash_plus(call.message.chat.id, call.message.message_id, fake_son)

async def update_qalampirlavash_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='qalampirlavash_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='qalampirlavash_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='qalampirlavash_savat'),
            ],
        ],
    )

    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

#-------------------mmolgoshtstandard-------------------#
@dp.callback_query_handler(text='mmolgoshtstandard_minus')
async def mmolgoshtstandard_minus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id, 1)
    print(fake_son)
    fake_son -= 1
    son[user_id] = fake_son
    await update_mmolgoshtstandard_minus(call.message.chat.id, call.message.message_id, fake_son)

async def update_mmolgoshtstandard_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='mmolgoshtstandard_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='mmolgoshtstandard_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='mmolgoshtstandard_savat'),
            ],
        ],
    )

    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

@dp.callback_query_handler(text='mmolgoshtstandard_plus')
async def mmolgoshtstandard_plus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id, 1)
    print(fake_son)
    fake_son += 1
    son[user_id] = fake_son
    await update_mmolgoshtstandard_plus(call.message.chat.id, call.message.message_id, fake_son)

async def update_mmolgoshtstandard_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='mmolgoshtstandard_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='mmolgoshtstandard_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='mmolgoshtstandard_savat'),
            ],
        ],
    )

    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

#-------------------standardcheese-------------------#
@dp.callback_query_handler(text='standardcheese_minus')
async def standardcheese_minus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id, 1)
    print(fake_son)
    fake_son -= 1
    son[user_id] = fake_son
    await update_mmolgoshtstandard_minus(call.message.chat.id, call.message.message_id, fake_son)

async def update_standardcheese_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='standardcheese_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='standardcheese_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='standardcheese_savat'),
            ],
        ],
    )

    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

@dp.callback_query_handler(text='standardcheese_plus')
async def standardcheese_plus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id, 1)
    print(fake_son)
    fake_son += 1
    son[user_id] = fake_son
    await update_mmolgoshtstandard_plus(call.message.chat.id, call.message.message_id, fake_son)

async def update_standardcheese_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='standardcheese_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='standardcheese_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='standardcheese_savat'),
            ],
        ],
    )

    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

#-------------------fitter-------------------#
@dp.callback_query_handler(text='fitter_minus',)
async def fitter_minus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id, 1)
    print(fake_son)
    fake_son -= 1
    son[user_id] = fake_son
    await update_fitter_minus(call.message.chat.id, call.message.message_id, fake_son)

async def update_fitter_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='fitter_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='fitter_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='fitter_savat'),
            ],
        ],
    )

    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

@dp.callback_query_handler(text='fitter_plus', state=Evos_state.menu_lavashlar)
async def fitter_plus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id, 1)
    print(fake_son)
    fake_son += 1
    son[user_id] = fake_son
    await update_fitter_plus(call.message.chat.id, call.message.message_id, fake_son)

async def update_fitter_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='fitter_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='fitter_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='fitter_savat'),
            ],
        ],
    )

    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

#-------------------tovuqgosht-------------------#

@dp.callback_query_handler(text='tovuqgosht_minus',)
async def tovuqgosht_minus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id, 2)
    print(fake_son)
    fake_son -= 1
    son[user_id] = fake_son
    await update_tovuqgosht_minus(call.message.chat.id, call.message.message_id, fake_son)

async def update_tovuqgosht_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='tovuqgosht_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='tovuqgosht_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='tovuqgosht_savat'),
            ],
        ],
    )

    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

@dp.callback_query_handler(text='tovuqgosht_plus',)
async def tovuqgosht_plus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id, 2)
    print(fake_son)
    fake_son += 1
    son[user_id] = fake_son
    await update_tovuqgosht_plus(call.message.chat.id, call.message.message_id, fake_son)

async def update_tovuqgosht_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='tovuqgosht_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='tovuqgosht_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='tovuqgosht_savat'),
            ],
        ],
    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)


#-------------------shaurmatovuqg-------------------#

@dp.callback_query_handler(text='shaurmatovuqg_minus')
async def shaurmatovuqg_minus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,2)
    print(fake_son)
    fake_son -= 1
    son[user_id] = fake_son
    await update_shaurmatovuqg_minus(call.message.chat.id, call.message.message_id, fake_son)

async def update_shaurmatovuqg_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖',callback_data='shaurmatovuqg_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='shaurmatovuqg_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='shaurmatovuqg_savat'),
            ],
        ],
    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

@dp.callback_query_handler(text='shaurmatovuqg_plus')
async def shaurmatovuqg_plus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,2)
    print(fake_son)
    fake_son += 1
    son[user_id] = fake_son
    await update_shaurmatovuqg_plus(call.message.chat.id, call.message.message_id, fake_son)

async def update_shaurmatovuqg_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖',callback_data='shaurmatovuqg_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='shaurmatovuqg_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='shaurmatovuqg_savat'),
            ],
        ],
    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)


#-------------------qmolgosht-------------------#

@dp.callback_query_handler(text='qmolgosht_minus')
async def qmolgosht_minus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,2)
    print(fake_son)
    fake_son -= 1
    son[user_id] = fake_son
    await update_qmolgosht_minus(call.message.chat.id, call.message.message_id, fake_son)

async def update_qmolgosht_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖',callback_data='qmolgosht_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='qmolgosht_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='qmolgosht_savat'),
            ],
        ],
    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

@dp.callback_query_handler(text='qmolgosht_plus')
async def qmolgosht_plus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,2)
    print(fake_son)
    fake_son += 1
    son[user_id] = fake_son
    await update_qmolgosht_plus(call.message.chat.id, call.message.message_id, fake_son)

async def update_qmolgosht_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖',callback_data='qmolgosht_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='qmolgosht_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='qmolgosht_savat'),
            ],
        ],
    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)


#-------------------qtovuqgosht-------------------#

@dp.callback_query_handler(text='qtovuqgosht_minus')
async def qtovuqgosht_minus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,2)
    print(fake_son)
    fake_son -= 1
    son[user_id] = fake_son
    await update_qtovuqgosht_minus(call.message.chat.id, call.message.message_id, fake_son)

async def update_qtovuqgosht_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖',callback_data='qtovuqgosht_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='qtovuqgosht_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='qtovuqgosht_savat'),
            ],
        ],
    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

@dp.callback_query_handler(text='qtovuqgosht_plus')
async def qtovuqgosht_plus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,2)
    print(fake_son)
    fake_son += 1
    son[user_id] = fake_son
    await update_qtovuqgosht_plus(call.message.chat.id, call.message.message_id, fake_son)

async def update_qtovuqgosht_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖',callback_data='qtovuqgosht_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='qtovuqgosht_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='qtovuqgosht_savat'),
            ],
        ],
    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

#-------------------shmolgosht-------------------#

@dp.callback_query_handler(text='shmolgosht_minus')
async def shmolgosht_minus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,2)
    print(fake_son)
    fake_son -= 1
    son[user_id] = fake_son
    await update_shmolgosht_minus(call.message.chat.id, call.message.message_id, fake_son)

async def update_shmolgosht_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖',callback_data='shmolgosht_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='shmolgosht_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='shmolgosht_savat'),
            ],
        ],
    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

@dp.callback_query_handler(text='shmolgosht_plus')
async def shmolgosht_plus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,2)
    print(fake_son)
    fake_son += 1
    son[user_id] = fake_son
    await update_shmolgosht_plus(call.message.chat.id, call.message.message_id, fake_son)

async def update_shmolgosht_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖',callback_data='shmolgosht_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='shmolgosht_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='shmolgosht_savat'),
            ],
        ],
    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

#-------------------gamburger-------------------#

@dp.callback_query_handler(text='gamburger_minus')
async def gamburger_minus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,3)
    print(fake_son)
    fake_son -= 1
    son[user_id] = fake_son
    await update_gamburger_minus(call.message.chat.id, call.message.message_id, fake_son)

async def update_gamburger_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖',callback_data='gamburger_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='gamburger_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='gamburger_savat'),
            ],
        ],
    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

@dp.callback_query_handler(text='gamburger_plus')
async def gamburger_plus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,3)
    print(fake_son)
    fake_son += 1
    son[user_id] = fake_son
    await update_gamburger_plus(call.message.chat.id, call.message.message_id, fake_son)

async def update_gamburger_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖',callback_data='gamburger_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='gamburger_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='gamburger_savat'),
            ],
        ],
    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)


#-------------------doubleburgere-------------------#

@dp.callback_query_handler(text='doubleburgere_minus')
async def doubleburgere_minus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,3)
    print(fake_son)
    fake_son -= 1
    son[user_id] = fake_son
    if fake_son <= 0:
        await call.answer("Maxsulot soni 0 dan kichik bolmasligi kerak")

    await update_doubleburgere_minus(call.message.chat.id, call.message.message_id, fake_son)

async def update_doubleburgere_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖',callback_data='doubleburgere_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='doubleburgere_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='doubleburgere_savat'),
            ],
        ],
    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

@dp.callback_query_handler(text='doubleburgere_plus')
async def doubleburgere_plus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,3)
    print(fake_son)
    fake_son += 1
    son[user_id] = fake_son
    await update_doubleburgere_plus(call.message.chat.id, call.message.message_id, fake_son)

async def update_doubleburgere_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖',callback_data='doubleburgere_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='doubleburgere_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='doubleburgere_savat'),
            ],
        ],
    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

#-------------------doublecheese-------------------#

@dp.callback_query_handler(text='doublecheese_minus')
async def doublecheese_minus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,3)
    print(fake_son)
    fake_son -= 1
    son[user_id] = fake_son
    if fake_son <= 0:
        await call.answer("Maxsulot soni 0 dan kichik bolmasligi kerak")
    await update_doublecheese_minus(call.message.chat.id, call.message.message_id, fake_son)

async def update_doublecheese_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖',callback_data='doublecheese_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='doublecheese_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='doublecheese_savat'),
            ],
        ],
    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

@dp.callback_query_handler(text='doublecheese_plus')
async def doublecheese_plus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,3)
    print(fake_son)
    fake_son += 1
    son[user_id] = fake_son
    await update_doublecheese_plus(call.message.chat.id, call.message.message_id, fake_son)

async def update_doublecheese_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖',callback_data='doublecheese_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='doublecheese_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='doublecheese_savat'),
            ],
        ],
    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)


#-------------------cheeseburger-------------------#

@dp.callback_query_handler(text='cheeseburger_minus')
async def cheeseburger_minus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,3)
    print(fake_son)
    fake_son -= 1
    son[user_id] = fake_son
    if fake_son <= 0:
        await call.answer("Maxsulot soni 0 dan kichik bolmasligi kerak")
    await update_cheeseburger_minus(call.message.chat.id, call.message.message_id, fake_son)

async def update_cheeseburger_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖',callback_data="cheeseburger_minus"),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='cheeseburger_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='cheeseburger_savat'),
            ],
        ],
    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

@dp.callback_query_handler(text='cheeseburger_plus')
async def cheeseburger_plus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,3)
    print(fake_son)
    fake_son += 1
    son[user_id] = fake_son
    await update_cheeseburger_plus(call.message.chat.id, call.message.message_id, fake_son)

async def update_cheeseburger_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖',callback_data="cheeseburger_minus"),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='cheeseburger_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='cheeseburger_savat'),
            ],
        ],
    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

#-------------------hotdogbagguate-------------------#

@dp.callback_query_handler(text='hotdogbagguate_minus')
async def hotdogbagguate_minus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,3)
    print(fake_son)
    fake_son -= 1
    son[user_id] = fake_son
    if fake_son <= 0:
        await call.answer("Maxsulot soni 0 dan kichik bolmasligi kerak")
    await update_hotdogbagguate_minus(call.message.chat.id, call.message.message_id, fake_son)

async def update_hotdogbagguate_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖',callback_data="hotdogbagguate_minus"),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='hotdogbagguate_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='hotdogbagguate_savat'),
            ],
        ],
    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

@dp.callback_query_handler(text='hotdogbagguate_plus')
async def hotdogbagguate_plus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,3)
    print(fake_son)
    fake_son += 1
    son[user_id] = fake_son
    await update_hotdogbagguate_plus(call.message.chat.id, call.message.message_id, fake_son)

async def update_hotdogbagguate_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖',callback_data="hotdogbagguate_minus"),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='hotdogbagguate_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='hotdogbagguate_savat'),
            ],
        ],
    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

#-------------------subtovuqcheese-------------------#

@dp.callback_query_handler(text='subtovuqcheese_minus')
async def subtovuqcheese_minus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,4)
    print(fake_son)
    fake_son -= 1
    son[user_id] = fake_son
    if fake_son <= 0:
        await call.answer("Maxsulot soni 0 dan kichik bolmasligi kerak")
    await update_subtovuqcheese_minus(call.message.chat.id, call.message.message_id, fake_son)

async def update_subtovuqcheese_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖',callback_data="subtovuqcheese_minus"),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='subtovuqcheese_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='subtovuqcheese_savat'),
            ],
        ],
    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

@dp.callback_query_handler(text='subtovuqcheese_plus')
async def subtovuqcheese_plus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,4)
    print(fake_son)
    fake_son += 1
    son[user_id] = fake_son
    await update_subtovuqcheese_plus(call.message.chat.id, call.message.message_id, fake_son)

async def update_subtovuqcheese_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖',callback_data="subtovuqcheese_minus"),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='subtovuqcheese_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='subtovuqcheese_savat'),
            ],
        ],
    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

#-------------------subtovuq-------------------#

@dp.callback_query_handler(text='subtovuq_minus')
async def subtovuq_minus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,4)
    print(fake_son)
    fake_son -= 1
    son[user_id] = fake_son
    if fake_son <= 0:
        await call.answer("Maxsulot soni 0 dan kichik bolmasligi kerak")
    await update_subtovuq_minus(call.message.chat.id, call.message.message_id, fake_son)

async def update_subtovuq_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖',callback_data="subtovuq_minus"),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='subtovuq_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='subtovuq_savat'),
            ],
        ],
    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

@dp.callback_query_handler(text='subtovuq_plus')
async def subtovuq_plus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,4)
    print(fake_son)
    fake_son += 1
    son[user_id] = fake_son
    await update_subtovuq_plus(call.message.chat.id, call.message.message_id, fake_son)

async def update_subtovuq_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖',callback_data="subtovuq_minus"),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='subtovuq_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='subtovuq_savat'),
            ],
        ],
    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

#-------------------hotdogbagguated-------------------#

@dp.callback_query_handler(text='hotdogbagguated_minus')
async def hotdogbagguated_minus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,4)
    print(fake_son)
    fake_son -= 1
    son[user_id] = fake_son
    if fake_son <= 0:
        await call.answer("Maxsulot soni 0 dan kichik bolmasligi kerak")
    await update_hotdogbagguated_minus(call.message.chat.id, call.message.message_id, fake_son)

async def update_hotdogbagguated_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖',callback_data="hotdogbagguated_minus"),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='hotdogbagguated_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='hotdogbagguated_savat'),
            ],
        ],
    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

@dp.callback_query_handler(text='hotdogbagguated_plus')
async def hotdogbagguated_plus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,4)
    print(fake_son)
    fake_son += 1
    son[user_id] = fake_son
    await update_hotdogbagguated_plus(call.message.chat.id, call.message.message_id, fake_son)

async def update_hotdogbagguated_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖',callback_data="hotdogbagguated_minus"),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='hotdogbagguated_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='hotdogbagguated_savat'),
            ],
        ],
    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

#-------------------hotdogkids-------------------#

@dp.callback_query_handler(text='hotdogkids_minus')
async def hotdogkids_minus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,4)
    print(fake_son)
    fake_son -= 1
    son[user_id] = fake_son
    if fake_son <= 0:
        await call.answer("Maxsulot soni 0 dan kichik bolmasligi kerak")
    await update_hotdogkids_minus(call.message.chat.id, call.message.message_id, fake_son)

async def update_hotdogkids_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖',callback_data="hotdogkids_minus"),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='hotdogkids_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='hotdogkids_savat'),
            ],
        ],
    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

@dp.callback_query_handler(text='hotdogkids_plus')
async def hotdogkids_plus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,4)
    print(fake_son)
    fake_son += 1
    son[user_id] = fake_son
    await update_hotdogkids_plus(call.message.chat.id, call.message.message_id, fake_son)

async def update_hotdogkids_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖',callback_data="hotdogkids_minus"),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='hotdogkids_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='hotdogkids_savat'),
            ],
        ],
    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

#-------------------subgoshtcheese-------------------#

@dp.callback_query_handler(text='subgoshtcheese_minus')
async def subgoshtcheese_minus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,5)
    print(fake_son)
    fake_son -= 1
    son[user_id] = fake_son
    if fake_son <= 0:
        await call.answer("Maxsulot soni 0 dan kichik bolmasligi kerak")
    await update_subgoshtcheese_minus(call.message.chat.id, call.message.message_id, fake_son)

async def update_subgoshtcheese_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data="subgoshtcheese_minus"),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='subgoshtcheese_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='subgoshtcheese_savat'),
            ],
        ],
    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

@dp.callback_query_handler(text='subgoshtcheese_plus')
async def subgoshtcheese_plus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,5)
    print(fake_son)
    fake_son += 1
    son[user_id] = fake_son
    await update_subgoshtcheese_plus(call.message.chat.id, call.message.message_id, fake_son)

async def update_subgoshtcheese_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data="subgoshtcheese_minus"),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='subgoshtcheese_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='subgoshtcheese_savat'),
            ],
        ],
    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)


#-------------------hotdogclasic-------------------#

@dp.callback_query_handler(text='hotdogclasic_minus')
async def hotdogclasic_minus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,5)
    print(fake_son)
    fake_son -= 1
    son[user_id] = fake_son
    if fake_son <= 0:
        await call.answer("Maxsulot soni 0 dan kichik bolmasligi kerak")
    await update_hotdogclasic_minus(call.message.chat.id, call.message.message_id, fake_son)

async def update_hotdogclasic_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data="hotdogclasic_minus"),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='hotdogclasic_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='hotdogclasic_savat'),
            ],
        ],
    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

@dp.callback_query_handler(text='hotdogclasic_plus')
async def hotdogclasic_plus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,5)
    print(fake_son)
    fake_son += 1
    son[user_id] = fake_son
    await update_hotdogclasic_plus(call.message.chat.id, call.message.message_id, fake_son)

async def update_hotdogclasic_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data="hotdogclasic_minus"),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='hotdogclasic_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='hotdogclasic_savat'),
            ],
        ],
    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

#-------------------sokdena-------------------#
@dp.callback_query_handler(text='sokdena_minus')
async def sokdena_minus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,6)
    print(fake_son)
    fake_son -= 1
    son[user_id] = fake_son
    if fake_son <= 0:
        await call.answer("Maxsulot soni 0 dan kichik bolmasligi kerak")

    await update_sokdena_minus(call.message.chat.id, call.message.message_id, fake_son)

async def update_sokdena_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data="sokdena_minus"),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='sokdena_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='sokdena_savat'),
            ],
        ],
    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

@dp.callback_query_handler(text='sokdena_plus')
async def sokdena_plus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,6)
    print(fake_son)
    fake_son += 1
    son[user_id] = fake_son
    await update_sokdena_plus(call.message.chat.id, call.message.message_id, fake_son)

async def update_sokdena_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data="sokdena_minus"),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='sokdena_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='sokdena_savat'),
            ],
        ],
    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)



@dp.callback_query_handler(text='sokdena_minus')
async def sokdena_minus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,6)
    print(fake_son)
    fake_son -= 1
    son[user_id] = fake_son
    if fake_son <= 0:
        await call.answer("Maxsulot soni 0 dan kichik bolmasligi kerak")

    await update_sokdena_minus(call.message.chat.id, call.message.message_id, fake_son)

async def update_sokdena_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data="sokdena_minus"),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='sokdena_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='sokdena_savat'),
            ],
        ],
    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

#-------------------pepsi05-------------------#
@dp.callback_query_handler(text='pepsi05_minus')
async def pepsi05_minus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,7)
    print(fake_son)
    fake_son -= 1
    son[user_id] = fake_son
    if fake_son <=0:
        await call.answer("Maxsulot soni 0 dan kichik bolmasligi kerak")
    await update_pepsi05_minus(call.message.chat.id, call.message.message_id, fake_son)

async def update_pepsi05_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data="pepsi05_minus"),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='pepsi05_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='pepsi05_savat'),
            ],
        ],
    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

@dp.callback_query_handler(text='pepsi05_plus')
async def pepsi05_plus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,7)
    print(fake_son)
    fake_son += 1
    son[user_id] = fake_son
    await update_pepsi05_plus(call.message.chat.id, call.message.message_id, fake_son)

async def update_pepsi05_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data="pepsi05_minus"),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='pepsi05_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='pepsi05_savat'),
            ],
        ],
    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)


#-------------------suv05-------------------#

@dp.callback_query_handler(text='suv05_minus')
async def suv05_minus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,8)
    print(fake_son)
    fake_son -= 1
    son[user_id] = fake_son
    if fake_son <=0:
        await call.answer("Maxsulot soni 0 dan kichik bolmasligi kerak")
    await update_suv05_minus(call.message.chat.id, call.message.message_id, fake_son)

async def update_suv05_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data="suv05_minus"),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='suv05_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='suv05_savat'),
            ],
        ],
    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

@dp.callback_query_handler(text='suv05_plus')
async def suv05_plus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,8)
    print(fake_son)
    fake_son += 1
    son[user_id] = fake_son
    await update_suv05_plus(call.message.chat.id, call.message.message_id, fake_son)

async def update_suv05_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data="suv05_minus"),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='suv05_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='suv05_savat'),
            ],
        ],
    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)



#-------------------pepsi15-------------------#

@dp.callback_query_handler(text='pepsi15_minus')
async def pepsi15_minus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,9)
    print(fake_son)
    fake_son -= 1
    son[user_id] = fake_son
    if fake_son <=0:
        await call.answer("Maxsulot soni 0 dan kichik bolmasligi kerak")
    await update_pepsi15_minus(call.message.chat.id, call.message.message_id, fake_son)

async def update_pepsi15_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data="pepsi15_minus"),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='pepsi15_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='pepsi15_savat'),
            ],
        ],
    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)


@dp.callback_query_handler(text='pepsi15_plus')
async def pepsi15_plus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,9)
    print(fake_son)
    fake_son += 1
    son[user_id] = fake_son
    await update_pepsi15_plus(call.message.chat.id, call.message.message_id, fake_son)

async def update_pepsi15_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data="pepsi15_minus"),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='pepsi15_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='pepsi15_savat'),
            ],
        ],
    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)


#-------------------quyibpepsi-------------------#

@dp.callback_query_handler(text='quyibpepsi_minus')
async def quyibpepsi_minus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,10)
    print(fake_son)
    fake_son -= 1
    son[user_id] = fake_son
    if fake_son <=0:
        await call.answer("Maxsulot soni 0 dan kichik bolmasligi kerak")
    await update_quyibpepsi_minus(call.message.chat.id, call.message.message_id, fake_son)

async def update_quyibpepsi_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖',callback_data="quyibpepsi_minus"),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='quyibpepsi_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='quyibpepsi_savat'),
            ],
        ],
    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

@dp.callback_query_handler(text='quyibpepsi_plus')
async def quyibpepsi_plus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,10)
    print(fake_son)
    fake_son += 1
    son[user_id] = fake_son
    await update_quyibpepsi_plus(call.message.chat.id, call.message.message_id, fake_son)

async def update_quyibpepsi_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖',callback_data="quyibpepsi_minus"),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='quyibpepsi_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='quyibpepsi_savat'),
            ],
        ],
    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)


#-------------------blisharbat-------------------#

@dp.callback_query_handler(text='blisharbat_minus')
async def blisharbat_minus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,11)
    print(fake_son)
    fake_son -= 1
    son[user_id] = fake_son
    if fake_son <=0:
        await call.answer("Maxsulot soni 0 dan kichik bolmasligi kerak")
    await update_blisharbat_minus(call.message.chat.id, call.message.message_id, fake_son)

async def update_blisharbat_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖',callback_data="blisharbat_minus"),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='blisharbat_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='blisharbat_savat'),
            ],
        ],
    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)


#-------------------Amerikano-------------------#
@dp.callback_query_handler(text='Amerikano_minus')
async def Amerikano_minus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,12)
    print(fake_son)
    fake_son -= 1
    son[user_id] = fake_son
    if fake_son <=0:
        await call.answer("Maxsulot soni 0 dan kichik bolmasligi kerak")
    await update_Amerikano_minus(call.message.chat.id, call.message.message_id, fake_son)

async def update_Amerikano_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖',callback_data="Amerikano_minus"),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='Amerikano_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='Amerikano_savat'),
            ],
        ],
    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

@dp.callback_query_handler(text='Amerikano_plus')
async def Amerikano_plus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,12)
    print(fake_son)
    fake_son += 1
    son[user_id] = fake_son
    await update_Amerikano_plus(call.message.chat.id, call.message.message_id, fake_son)

async def update_Amerikano_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖',callback_data="Amerikano_minus"),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='Amerikano_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='Amerikano_savat'),
            ],
        ],
    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)


#-------------------lattle-------------------#
@dp.callback_query_handler(text='lattle_minus')
async def lattle_minus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,13)
    print(fake_son)
    fake_son -= 1
    son[user_id] = fake_son
    if fake_son <=0:
        await call.answer("Maxsulot soni 0 dan kichik bolmasligi kerak")
    await update_lattle_minus(call.message.chat.id, call.message.message_id, fake_son)

async def update_lattle_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖',callback_data="lattle_minus"),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='lattle_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='lattle_savat'),
            ],
        ],
    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

@dp.callback_query_handler(text='lattle_plus')
async def lattle_plus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,13)
    print(fake_son)
    fake_son += 1
    son[user_id] = fake_son
    await update_lattle_plus(call.message.chat.id, call.message.message_id, fake_son)

async def update_lattle_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖',callback_data="lattle_minus"),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='lattle_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='lattle_savat'),
            ],
        ],
    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

#-------------------kokchoy-------------------#
@dp.callback_query_handler(text='kokchoy_minus')
async def kokchoy_minus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,14)
    print(fake_son)
    fake_son -= 1
    son[user_id] = fake_son
    if fake_son <=0:
        await call.answer("Maxsulot soni 0 dan kichik bolmasligi kerak")
    await update_kokchoy_minus(call.message.chat.id, call.message.message_id, fake_son)

async def update_kokchoy_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖',callback_data="kokchoy_minus"),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='kokchoy_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='kokchoy_savat'),
            ],
        ],
    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

@dp.callback_query_handler(text='kokchoy_plus')
async def kokchoy_plus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,14)
    print(fake_son)
    fake_son += 1
    son[user_id] = fake_son
    await update_kokchoy_plus(call.message.chat.id, call.message.message_id, fake_son)

async def update_kokchoy_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖',callback_data="kokchoy_minus"),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='kokchoy_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='kokchoy_savat'),
            ],
        ],
    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)


#-------------------qorachoyo-------------------#

@dp.callback_query_handler(text='qorachoyo_minus')
async def qorachoyo_minus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,15)
    print(fake_son)
    fake_son -= 1
    son[user_id] = fake_son
    if fake_son <=0:
        await call.answer("Maxsulot soni 0 dan kichik bolmasligi kerak")
    await update_qorachoyo_minus(call.message.chat.id, call.message.message_id, fake_son)

async def update_qorachoyo_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖',callback_data="qorachoyo_minus"),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='qorachoyo_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='qorachoyo_savat'),
            ],
        ],
    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

@dp.callback_query_handler(text='qorachoyo_plus')
async def qorachoyo_plus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,15)
    print(fake_son)
    fake_son += 1
    son[user_id] = fake_son
    await update_qorachoyo_plus(call.message.chat.id, call.message.message_id, fake_son)

async def update_qorachoyo_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖',callback_data="qorachoyo_minus"),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='qorachoyo_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='qorachoyo_savat'),
            ],
        ],

    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)


#-------------------limonchoy-------------------#
@dp.callback_query_handler(text='limonchoy_minus')
async def limonchoy_minus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,16)
    print(fake_son)
    fake_son -= 1
    son[user_id] = fake_son
    if fake_son <=0:
        await call.answer("Maxsulot soni 0 dan kichik bolmasligi kerak")
    await update_limonchoy_minus(call.message.chat.id, call.message.message_id, fake_son)

async def update_limonchoy_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖',callback_data='limonchoy_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='limonchoy_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='limonchoy_savat'),
            ],
        ],

    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

@dp.callback_query_handler(text='limonchoy_plus')
async def limonchoy_plus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,16)
    print(fake_son)
    fake_son += 1
    son[user_id] = fake_son
    await update_limonchoy_plus(call.message.chat.id, call.message.message_id, fake_son)

async def update_limonchoy_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖',callback_data='limonchoy_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='limonchoy_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='limonchoy_savat'),
            ],
        ],

    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

#-------------------asalim-------------------#
@dp.callback_query_handler(text='asalim_minus')
async def asalim_minus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,17)
    print(fake_son)
    fake_son -= 1
    son[user_id] = fake_son
    if fake_son <= 0:
        await call.answer("Maxsulot soni 0 dan kichik bolmasligi kerak")
    await update_asalim_minus(call.message.chat.id, call.message.message_id, fake_son)

async def update_asalim_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='asalim_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='asalim_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='asalim_savat'),
            ],
        ],

    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

@dp.callback_query_handler(text='asalim_plus')
async def asalim_plus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,17)
    print(fake_son)
    fake_son += 1
    son[user_id] = fake_son
    await update_asalim_plus(call.message.chat.id, call.message.message_id, fake_son)

async def update_asalim_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='asalim_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='asalim_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='asalim_savat'),
            ],
        ],

    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)


#-------------------chizkeyk-------------------#
@dp.callback_query_handler(text='chizkeyk_minus')
async def chizkeyk_minus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,18)
    print(fake_son)
    fake_son -= 1
    son[user_id] = fake_son
    if fake_son <= 0:
        await call.answer("Maxsulot soni 0 dan kichik bolmasligi kerak")
    await update_chizkeyk_minus(call.message.chat.id, call.message.message_id, fake_son)

async def update_chizkeyk_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='chizkeyk_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='chizkeyk_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='chizkeyk_savat'),
            ],
        ],

    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)


#-------------------karamelin-------------------#
@dp.callback_query_handler(text='karamelin_minus')
async def karamelin_minus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,19)
    print(fake_son)
    fake_son -= 1
    son[user_id] = fake_son
    if fake_son <= 0:
        await call.answer("Maxsulot soni 0 dan kichik bolmasligi kerak")
    await update_karamelin_minus(call.message.chat.id, call.message.message_id, fake_son)

async def update_karamelin_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='karamelin_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='karamelin_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='karamelin_savat'),
            ],
        ],

    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

@dp.callback_query_handler(text='karamelin_plus')
async def karamelin_plus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,19)
    print(fake_son)
    fake_son += 1
    son[user_id] = fake_son
    await update_karamelin_plus(call.message.chat.id, call.message.message_id, fake_son)

async def update_karamelin_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='karamelin_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='karamelin_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='karamelin_savat'),
            ],
        ],

    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

#-------------------mevali-------------------#
@dp.callback_query_handler(text='mevali_minus')
async def mevali_minus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,20)
    print(fake_son)
    fake_son -= 1
    son[user_id] = fake_son
    if fake_son <= 0:
        await call.answer("Maxsulot soni 0 dan kichik bolmasligi kerak")
    await update_mevali_minus(call.message.chat.id, call.message.message_id, fake_son)

async def update_mevali_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='mevali_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='mevali_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='mevali_savat'),
            ],
        ],

    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

@dp.callback_query_handler(text='mevali_plus')
async def mevali_plus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,20)
    print(fake_son)
    fake_son += 1
    son[user_id] = fake_son
    await update_mevali_plus(call.message.chat.id, call.message.message_id, fake_son)

async def update_mevali_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='mevali_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='mevali_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='mevali_savat'),
            ],
        ],

    )

    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

#-------------------ketchup-------------------#
@dp.callback_query_handler(text='ketchup_minus')
async def ketchup_minus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,21)
    print(fake_son)
    fake_son -= 1
    son[user_id] = fake_son
    if fake_son <= 0:
        await call.answer("Maxsulot soni 0 dan kichik bolmasligi kerak")
    await update_ketchup_minus(call.message.chat.id, call.message.message_id, fake_son)

async def update_ketchup_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='ketchup_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='ketchup_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='ketchup_savat'),
            ],
        ],

    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)



@dp.callback_query_handler(text='ketchup_plus')
async def ketchup_plus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,21)
    print(fake_son)
    fake_son += 1
    son[user_id] = fake_son
    await update_ketchup_plus(call.message.chat.id, call.message.message_id, fake_son)

async def update_ketchup_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='ketchup_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='ketchup_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='ketchup_savat'),
            ],
        ],

    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

#-------------------garnir-------------------#
@dp.callback_query_handler(text='garnir_minus')
async def garnir_minus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,22)
    print(fake_son)
    fake_son -= 1
    son[user_id] = fake_son
    if fake_son <= 0:
        await call.answer("Maxsulot soni 0 dan kichik bolmasligi kerak")
    await update_garnir_minus(call.message.chat.id, call.message.message_id, fake_son)

async def update_garnir_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='garnir_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='garnir_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='garnir_savat'),
            ],
        ],

    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

@dp.callback_query_handler(text='garnir_plus')
async def garnir_plus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,22)
    print(fake_son)
    fake_son += 1
    son[user_id] = fake_son
    await update_garnir_plus(call.message.chat.id, call.message.message_id, fake_son)

async def update_garnir_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='garnir_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='garnir_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='garnir_savat'),
            ],
        ],

    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

#-------------------tovuqstrips-------------------#
@dp.callback_query_handler(text='tovuqstrips_minus')
async def tovuqstrips_minus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,23)
    print(fake_son)
    fake_son -= 1
    son[user_id] = fake_son
    if fake_son <= 0:
        await call.answer("Maxsulot soni 0 dan kichik bolmasligi kerak")
    await update_tovuqstrips_minus(call.message.chat.id, call.message.message_id, fake_son)

async def update_tovuqstrips_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='tovuqstrips_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='tovuqstrips_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='tovuqstrips_savat'),
            ],
        ],

    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)


@dp.callback_query_handler(text='tovuqstrips_plus')
async def tovuqstrips_plus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,23)
    print(fake_son)
    fake_son += 1
    son[user_id] = fake_son
    await update_tovuqstrips_plus(call.message.chat.id, call.message.message_id, fake_son)

async def update_tovuqstrips_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='tovuqstrips_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='tovuqstrips_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='tovuqstrips_savat'),
            ],
        ],

    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)


#-------------------pishloqli_sous-------------------#
@dp.callback_query_handler(text='pishloqli_sous_minus')
async def pishloqli_sous_minus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,24)
    print(fake_son)
    fake_son -= 1
    son[user_id] = fake_son
    if fake_son <= 0:
        await call.answer("Maxsulot soni 0 dan kichik bolmasligi kerak")
    await update_pishloqli_sous_minus(call.message.chat.id, call.message.message_id, fake_son)

async def update_pishloqli_sous_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖',callback_data='pishloqli_sous_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='pishloqli_sous_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='pishloqli_sous_savat'),
            ],
        ],

    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

@dp.callback_query_handler(text='pishloqli_sous_plus')
async def pishloqli_sous_plus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,24)
    print(fake_son)
    fake_son += 1
    son[user_id] = fake_son
    await update_pishloqli_sous_plus(call.message.chat.id, call.message.message_id, fake_son)

async def update_pishloqli_sous_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖',callback_data='pishloqli_sous_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='pishloqli_sous_plus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='pishloqli_sous_savat'),
            ],
        ],

    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)


#-------------------chisnokli_sous-------------------#
@dp.callback_query_handler(text='chisnokli_sous_minus')
async def chisnokli_sous_minus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,25)
    print(fake_son)
    fake_son -= 1
    son[user_id] = fake_son
    if fake_son<=0:
        await call.answer("Maxsulot soni 0 dan kichik bolmasligi kerak")
    await update_chisnokli_sous_minus(call.message.chat.id, call.message.message_id, fake_son)

async def update_chisnokli_sous_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➕', callback_data='chisnokli_sous_plus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➖', callback_data='chisnokli_sous_minus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='chisnokli_sous_savat'),
            ],
        ],

    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)


@dp.callback_query_handler(text='chisnokli_sous_plus')
async def chisnokli_sous_plus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,25)
    print(fake_son)
    fake_son += 1
    son[user_id] = fake_son
    await update_chisnokli_sous_plus(call.message.chat.id, call.message.message_id, fake_son)

async def update_chisnokli_sous_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➕',callback_data='chisnokli_sous_plus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➖', callback_data='chisnokli_sous_minus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='chisnokli_sous_savat'),
            ],
        ],

    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)


#-------------------chilisous-------------------#
@dp.callback_query_handler(text='chilisous_minus')
async def chilisous_minus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,26)
    print(fake_son)
    fake_son -= 1
    son[user_id] = fake_son
    if fake_son<=0:
        await call.answer("Maxsulot soni 0 dan kichik bolmasligi kerak")
    await update_chilisous_minus(call.message.chat.id, call.message.message_id, fake_son)

async def update_chilisous_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➕', callback_data='chilisous_plus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➖', callback_data='chilisous_minus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='chilisous_savat'),
            ],
        ],

    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

@dp.callback_query_handler(text='chilisous_plus')
async def chilisous_plus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,26)
    print(fake_son)
    fake_son += 1
    son[user_id] = fake_son
    await update_chilisous_plus(call.message.chat.id, call.message.message_id, fake_son)

async def update_chilisous_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➕',callback_data='chilisous_plus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➖', callback_data='chilisous_minus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='chilisous_savat'),
            ],
        ],

    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)


#-------------------barbekusous-------------------#
@dp.callback_query_handler(text='barbekusous_minus')
async def barbekusous_minus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,27)
    print(fake_son)
    fake_son -= 1
    son[user_id] = fake_son
    if fake_son<=0:
        await call.answer("Maxsulot soni 0 dan kichik bolmasligi kerak")
    await update_barbekusous_minus(call.message.chat.id, call.message.message_id, fake_son)

async def update_barbekusous_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➕', callback_data='barbekusous_plus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➖', callback_data='barbekusous_minus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='barbekusous_savat'),
            ],
        ],

    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)


@dp.callback_query_handler(text='barbekusous_plus')
async def barbekusous_plus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,27)
    print(fake_son)
    fake_son += 1
    son[user_id] = fake_son
    await update_barbekusous_plus(call.message.chat.id, call.message.message_id, fake_son)

async def update_barbekusous_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➕',callback_data='barbekusous_plus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➖', callback_data='barbekusous_minus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='barbekusous_savat'),
            ],
        ],

    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)


#-------------------salat-------------------#
@dp.callback_query_handler(text='salat_minus')
async def salat_minus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,28)
    print(fake_son)
    fake_son -= 1
    son[user_id] = fake_son
    if fake_son<=0:
        await call.answer("Maxsulot soni 0 dan kichik bolmasligi kerak")
    await update_salat_minus(call.message.chat.id, call.message.message_id, fake_son)

async def update_salat_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➕', callback_data='salat_plus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➖', callback_data='salat_minus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='salat_savat'),
            ],
        ],

    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)


@dp.callback_query_handler(text='salat_plus')
async def salat_plus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,28)
    print(fake_son)
    fake_son += 1
    son[user_id] = fake_son
    await update_salat_plus(call.message.chat.id, call.message.message_id, fake_son)

async def update_salat_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➕',callback_data='salat_plus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➖', callback_data='salat_minus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='salat_savat'),
            ],
        ],

    )

    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)


#-------------------non-------------------#
@dp.callback_query_handler(text='non_minus')
async def non_minus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,29)
    print(fake_son)
    fake_son -= 1
    son[user_id] = fake_son
    if fake_son<=0:
        await call.answer("Maxsulot soni 0 dan kichik bolmasligi kerak")
    await update_non_minus(call.message.chat.id, call.message.message_id, fake_son)

async def update_non_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➕', callback_data='non_plus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➖', callback_data='non_minus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='non_savat'),
            ],
        ],

    )
    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)

@dp.callback_query_handler(text='non_plus')
async def non_plus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,29)
    print(fake_son)
    fake_son += 1
    son[user_id] = fake_son
    await update_non_plus(call.message.chat.id, call.message.message_id, fake_son)

async def update_non_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➕',callback_data='non_plus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➖', callback_data='non_minus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='non_savat'),
            ],
        ],

    )

    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)
    

#-------------------fri-------------------#

@dp.callback_query_handler(text='fri_plus')
async def fri_plus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,29)
    print(fake_son)
    fake_son += 1
    son[user_id] = fake_son
    await update_fri_plus(call.message.chat.id, call.message.message_id, fake_son)

async def update_fri_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➕',callback_data='fri_plus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➖', callback_data='fri_minus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='fri_savat'),
            ],
        ],

    )

    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)


@dp.callback_query_handler(text='fri_minus')
async def fri_minus(call:types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,29)
    print(fake_son)
    fake_son -= 1
    son[user_id] = fake_son
    if fake_son<=0:
        await call.answer("Maxsulot soni 0 dan kichik bolmasligi kerak")
    await update_fri_minus(call.message.chat.id, call.message.message_id, fake_son)


async def update_fri_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➕', callback_data='fri_plus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➖', callback_data='fri_minus')
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='fri_savat'),
            ],
        ],

    )

    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)



#-------------------------subgosht-------------------------#

@dp.callback_query_handler(text='subgosht_plus')
async def subgosht_plus(call: types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,29)
    print(fake_son)
    fake_son += 1
    son[user_id] = fake_son
    await update_subgosht_plus(call.message.chat.id, call.message.message_id, fake_son)

async def update_subgosht_plus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='subgosht_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕',callback_data='subgosht_plus'),
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='subgosht_savat'),
            ],
        ],

    )

    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)


@dp.callback_query_handler(text='subgosht_minus')
async def subgosht_minus(call:types.CallbackQuery):
    user_id = str(call.message.chat.id)
    print(user_id)
    fake_son = son.get(user_id,29)
    print(fake_son)
    fake_son -= 1
    son[user_id] = fake_son
    if fake_son<=0:
        await call.answer("Maxsulot soni 0 dan kichik bolmasligi kerak")
    await update_subgosht_minus(call.message.chat.id, call.message.message_id, fake_son)


async def update_subgosht_minus(chat_id, message_id, new_son):
    new_buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('➖', callback_data='subgosht_minus'),
                InlineKeyboardButton(f"{new_son}", callback_data='son'),
                InlineKeyboardButton('➕', callback_data='subgosht_plus'),
            ],
            [
                InlineKeyboardButton("Savatga qo'shish", callback_data='fri_savat'),
            ],
        ],

    )

    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=new_buttons)