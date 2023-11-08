from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
from bot import dp, Evos_state, bot, son
from aiogram.dispatcher import FSMContext
from bot import Evos_state


@dp.message_handler(text='Buyurtma berish 🚚',state=Evos_state.buyurtma_berish)
async def buyurtma_berish(message:types.Message,state:FSMContext):
    await message.answer("Buyurtmangiz qabul qilindi",reply_markup=ReplyKeyboardRemove())
    await state.finish()

