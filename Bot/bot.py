import logging
from aiogram import executor
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardRemove

from Keyboards.default import number_p, location, all_buttons, menu, menusetlarrr, lavashssss, shaurma, burgerss, \
    hotgodsss, ichimliklarr
from Keyboards.inline import comboqorachoy, fitcombooo, iftar, donakboksss, com_bo, lavash2, pishloqlig, cheese_buttons, \
    cheese_buttons2, shaurma_, burgerassdf, hotdog_button, ichimliklar_button

API_TOKEN = '6420073648:AAEh4AowCPo90xm4tJl0rJ_no7Xi4-ZLpO8'

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())


class Evos_state(StatesGroup):
    phone_number = State()
    location = State()
    menu = State()
    menu_setlar = State()
    menu_lavashlar = State()
    menu_shaurma = State()
    menu_burger = State()
    menu_hotdog = State()
    menu_ichimliklar = State()


son = {
    'user_id': 1
}


@dp.message_handler(commands='start')
async def command1(message: types.Message, state: FSMContext):
    son[message.from_user.id] = 1
    print(son)
    await message.answer('<b>EVOS | Доставка</b> botiga xush kelibsiz!')
    await message.answer('''
Avval telefon raqamingizni yuboring,
yoki <b>+998XX XXXXXXX</b> ko'rinishida yozing.

<a href="https://evos.uz/uz/about/">Evos</a>    
    ''', reply_markup=number_p)
    await Evos_state.phone_number.set()


@dp.message_handler(content_types=types.ContentType.CONTACT, state=Evos_state.phone_number)
async def phone_number(message: types.Message, state: FSMContext):
    await message.answer('<b>Iltimos joylashuvni yuboring!</b>', reply_markup=location)
    await state.finish()
    await Evos_state.location.set()


@dp.message_handler(content_types=types.ContentType.LOCATION, state=Evos_state.location)
async def user_location(message: types.Message, state: FSMContext):
    await message.answer('<b>EVOS | Доставка</b>botiga xush kelibsiz!', reply_markup=all_buttons)
    await state.finish()
    await Evos_state.menu.set()


@dp.message_handler(text='Menu 🍴', state=Evos_state.menu)
async def menyu(message: types.Message, state: FSMContext):
    await message.answer('Tanlang:', reply_markup=menu)
    await state.finish()

#-------------------------Setlar-------------------------#


@dp.message_handler(text='Setlar (8)')
async def menusetlar(message: types.Message, state: FSMContext):
    photo = open('Images/setlar-menu.jpg', 'rb')
    await message.answer_photo(photo=photo, reply_markup=menusetlarrr)
    await Evos_state.menu_setlar.set()


@dp.message_handler(text='Combo Plus Isituvchan (Qora choy)', state=Evos_state.menu_setlar)
async def qora_choy(message: types.Message):
    photo = open('Images/qorachoy+.jpg', 'rb')
    await message.answer_photo(photo=photo, reply_markup=comboqorachoy, caption="Narxi: 16 000 so'm")

@dp.message_handler(text='FitCombo',state=Evos_state.menu_setlar)
async def fitcombooooo(message:types.Message):
    photo = open('Images/fitcombo.jpg', 'rb')
    await message.answer_photo(photo=photo, reply_markup=fitcombooo, caption="Narxi: 30 000 so'm")

@dp.message_handler(text="Iftar kofte grill mol go'shtidan",state=Evos_state.menu_setlar)
async def iftarkofte(message:types.Message):
    photo = open('Images/iftarkofte.jpg', 'rb')
    await message.answer_photo(photo=photo, reply_markup=iftar, caption='''
Muborak RAMAZON oyi munosabati
bilan maxsus taklif! Mol go'shtli 
5 dona shirali gril-kotletlari, guruch, 
limon sharbati bilan boyitilgan qizil karamli 
salat, pomidorlar va yong'oqlardan tayyorlangan 
maxsus quyuq RAMAZON sousi. Iftorlik 
vaqtingiz uchun ideal yechim!
Narxi: 35 000 so'm    
    ''',)

@dp.message_handler(text="Donar boks  mol go'shtidan",state=Evos_state.menu_setlar)
async def donarboks(message:types.Message):
    photo = open('Images/donarboks.jpg', 'rb')
    await message.answer_photo(photo=photo, reply_markup=donakboksss, caption='''
YANGILIK! Oq kunjut sousi ostidagi shirali grill tovuq go'shti, qarsildoq kartoshka-fri, donador guruch, qizil karamdan tayyorlangan barra salatdan tashkil topgan qatlamlarning to'yimli uyg'unlashuvi. Qulay, ixcham, ammo to'yimli qadoq!
Narxi: 34 000 so'm    
    ''')

@dp.message_handler(text="COMBO+",state=Evos_state.menu_setlar)
async def donarboks(message:types.Message):
    photo = open('Images/com+bo.jpg', 'rb')
    await message.answer_photo(photo=photo, reply_markup=com_bo, caption='''
Yeng yaxshi taklif! Issiq qarsildoq qovurilgan kartoshka va bir stakan Pepsi
Narxi: 16 000 so'm    
    ''')


@dp.message_handler(text="Donar boks tovuq go'shtidan",state=Evos_state.menu_setlar)
async def donarboks(message:types.Message):
    photo = open('Images/donartovuq.jpg', 'rb')
    await message.answer_photo(photo=photo, reply_markup=com_bo, caption='''
YANGILIK!  Yangi, maxsus tayyorlangan teriyaki sousi, grill tovuq go'shti, qarsildoq kartoshka-fri, donador guruch, limon sharbati bilan to'yintirilgan qizil karamdan tayyorlangan barra salatning noodatiy mazali uyg'unlashuvi. Qulay, ixcham, ammo to'yimli qadoq!
Narxi: 32 000 so'm
    ''')



@dp.message_handler(text="Iftar strips tovuq go'shtidan",state=Evos_state.menu_setlar)
async def donarboks(message:types.Message):
    photo = open('Images/iftartovuq.jpg', 'rb')
    await message.answer_photo(photo=photo, reply_markup=com_bo, caption='''
Muborak RAMAZON oyi munosabati bilan maxsus taklif! Tovuqli 5 dona shirali gril-kotletlari, guruch, limon sharbati bilan boyitilgan qizil karamli salat, pomidorlar va yong'oqlardan tayyorlangan maxsus quyuq RAMAZON sousi. Iftorlik vaqtingiz uchun ideal yechim!
Narxi: 30 000 so'm
    ''')

@dp.message_handler(text="Kids COMBO",state=Evos_state.menu_setlar)
async def donarboks(message:types.Message):
    photo = open('Images/kidscombo.jpg', 'rb')
    await message.answer_photo(photo=photo, reply_markup=com_bo, caption='''
Narxi: 16 000 so'm
    ''')

@dp.message_handler(text='Orqaga qaytish 🔙', state=Evos_state.menu_setlar)
async def menyu(message: types.Message, state: FSMContext):
    await message.answer('Tanlang:', reply_markup=menu)
    await state.finish()


#----------------------Lavash----------------------#





@dp.message_handler(text='Lavash (9)')
async def lavashalar(message:types.Message,state:FSMContext):
    photo = open('Images/lavashs.jpg', 'rb')
    await message.answer_photo(photo=photo, reply_markup=lavashssss)
    await Evos_state.menu_lavashlar.set()



@dp.message_handler(text='Mol goʼshtidan qalampir lavash',state=Evos_state.menu_lavashlar)
async def lavashlar(message:types.Message):
    photo = open('Images/qalampirlavash.jpg', 'rb')
    await message.answer_photo(photo=photo, reply_markup=lavash2,caption='''
Qarsildoq chipslar, yangi bodring va pomidorlar bilan lavashga oʼralgan yumshoq mol goʼshti, bizning taʼmi oʼtkir qayla bilan
Narxi: 26 000 so'm    
    ''')

@dp.message_handler(text='Tovuq goʼshtli qalampir lavash',state=Evos_state.menu_lavashlar)
async def lavashlar(message:types.Message):
    photo = open('Images/goshtgalampir.jpg', 'rb')
    await message.answer_photo(photo=photo, reply_markup=lavash2,caption='''
Yangi bodring va pomidorlar, qarsildoq chipslar bilan lavashga oʼralgan qovurilgan tovuq filesi, bizning taʼmi oʼtkir maxsus qayla bilan
Narxi: 24 000 so'm    
    ''')

@dp.message_handler(text='Mol goʼshtidan pishloqli lavash Standard',state=Evos_state.menu_lavashlar)
async def lavashlar(message:types.Message):
    photo = open('Images/lavashstandard.jpg', 'rb')
    await message.answer_photo(photo=photo, reply_markup=pishloqlig,caption='''
Tanlang:  
    ''')


@dp.callback_query_handler(text='mini',state=Evos_state.menu_lavashlar)
async def mini(call:types.CallbackQuery):
    await call.message.delete()
    photo = open('Images/lavashstandard.jpg', 'rb')
    await call.message.answer_photo(photo=photo, reply_markup=lavash2, caption="Mini go'shtidan pishloqli lavash\n\nNarx: 25 000 so'm")

@dp.callback_query_handler(text='big',state=Evos_state.menu_lavashlar)
async def mini(call:types.CallbackQuery):
    await call.message.delete()
    photo = open('Images/lavashstandard.jpg', 'rb')
    await call.message.answer_photo(photo=photo, reply_markup=lavash2, caption="Big go'shtidan pishloqli lavash\n\nNarx: 29 000 so'm")

@dp.message_handler(text="Lavash cheese tovuq go'sht Standart",state=Evos_state.menu_lavashlar)
async def mini(message:types.Message):
    photo = open('Images/cheesetovuq.jpg', 'rb')
    await message.answer_photo(photo=photo, reply_markup=cheese_buttons)
@dp.callback_query_handler(text='mini23',state=Evos_state.menu_lavashlar)
async def mini(call:types.CallbackQuery):
    await call.message.delete()
    photo = open('Images/cheesetovuq.jpg', 'rb')
    await call.message.answer_photo(photo=photo, reply_markup=lavash2, caption="Mini tovuq pishloqli lavash\n\nNarx: 23 000 so'm")

@dp.callback_query_handler(text='big27',state=Evos_state.menu_lavashlar)
async def mini(call:types.CallbackQuery):
    await call.message.delete()
    photo = open('Images/cheesetovuq.jpg', 'rb')
    await call.message.answer_photo(photo=photo, reply_markup=lavash2, caption="Big tovuq pishloqli lavash\n\nNarx: 27 000 so'm")

@dp.message_handler(text='FITTER',state=Evos_state.menu_lavashlar)
async def lavashlar(message:types.Message):
    photo = open('Images/fitter.jpg', 'rb')
    await message.answer_photo(photo=photo, reply_markup=lavash2, caption='''
Tovuq goʼshti, qarsildoq muztogʼ salati, yangi bodring va pomidorlar, fetaksa va bizning maxsus qaylamiz - barchasi yashil lavashga oʼralgan
Narxi: 22 000 so'm    
    ''')

@dp.message_handler(text="Lavash tovuq go'sht",state=Evos_state.menu_lavashlar)
async def mini(message:types.Message):
    photo = open('Images/tovuqgoshtbigmin.jpg', 'rb')
    await message.answer_photo(photo=photo, reply_markup=cheese_buttons2,caption="Tanlang:" )

@dp.callback_query_handler(text="mini20",state=Evos_state.menu_lavashlar)
async def mini(call:types.CallbackQuery):
    await call.message.delete()
    photo = open('Images/tovuqgoshtbigmin.jpg', 'rb')
    await call.message.answer_photo(photo=photo, reply_markup=lavash2,caption="Narx: 20 000 so'm" )

@dp.callback_query_handler(text="big24",state=Evos_state.menu_lavashlar)
async def mini(call:types.CallbackQuery):
    await call.message.delete()
    photo = open('Images/tovuqgoshtbigmin.jpg', 'rb')
    await call.message.answer_photo(photo=photo, reply_markup=lavash2,caption="Narx: 24 000 so'm"  )

@dp.message_handler(text='Orqaga qaytish 🔙', state=Evos_state.menu_lavashlar)
async def menyu(message: types.Message, state: FSMContext):
    await message.answer('Tanlang:', reply_markup=menu)
    await state.finish()

#----------------------shaurma----------------------#





@dp.message_handler(text='Shaurma (4)')
async def shaurmaaa(message:types.Message,state:FSMContext):
    photo = open('Images/shaurma.jpg', 'rb')
    await message.answer_photo(photo=photo, reply_markup=shaurma)
    await Evos_state.menu_shaurma.set()

@dp.message_handler(text="Shaurma tovuq go'sht",state=Evos_state.menu_shaurma)
async def shaurmaadsgasd(message:types.Message,state:FSMContext):
    photo = open('Images/shurma2.jpg', 'rb')
    await message.answer_photo(photo=photo, reply_markup=shaurma_,caption="Narx: 24 000 so'm")

@dp.message_handler(text="Shaurma qalampir mol go'sht",state=Evos_state.menu_shaurma)
async def shaurmassasd(message:types.Message,state:FSMContext):
    photo = open('Images/shurma.jpg', 'rb')
    await message.answer_photo(photo=photo, reply_markup=shaurma_,caption="Narx: 22 000 so'm")

@dp.message_handler(text="Shaurma qalampir tovuq go'sht",state=Evos_state.menu_shaurma)
async def shaurmasdgasa(message:types.Message,state:FSMContext):
    photo = open('Images/shurma2.jpg', 'rb')
    await message.answer_photo(photo=photo, reply_markup=shaurma_,caption="Narx: 26 000 so'm")

@dp.message_handler(text="Shaurma mol go'sht",state=Evos_state.menu_shaurma)
async def shauasdgasdrma(message:types.Message,state:FSMContext):
    photo = open('Images/shurma.jpg', 'rb')
    await message.answer_photo(photo=photo, reply_markup=shaurma_,caption="Narx: 24 000 so'm")

@dp.message_handler(text="Ortga qaytish 🔙",state=Evos_state.menu_shaurma)
async def menyu(message: types.Message, state: FSMContext):
    await message.answer('Tanlang:', reply_markup=menu)
    await state.finish()


#-------------------------Burger-------------------------#

@dp.message_handler(text="Burger (4)")
async def burger(message:types.Message,state:FSMContext):
    photo = open("Images/burgers.jpg","rb")
    await message.answer_photo(photo=photo,reply_markup=burgerss)
    await Evos_state.menu_burger.set()


@dp.message_handler(text='Gamburger',state=Evos_state.menu_burger)
async def burger_thing(message:types.Message):
    photo = open("Images/gamburger.jpg", "rb")
    await message.answer_photo(photo=photo, reply_markup=burgerassdf,caption="Narx: 22 000 so'm")

@dp.message_handler(text='Double burger',state=Evos_state.menu_burger)
async def burger_thing(message:types.Message):
    photo = open("Images/doubleburger.jpg", "rb")
    await message.answer_photo(photo=photo, reply_markup=burgerassdf,caption="Narx: 33 000 so'm")


@dp.message_handler(text='Double cheese',state=Evos_state.menu_burger)
async def burger_thing(message:types.Message):
    photo = open("Images/dcheeseburger.jpg", "rb")
    await message.answer_photo(photo=photo, reply_markup=burgerassdf,caption="Narx: 37 000 so'm")
@dp.message_handler(text='Cheese burger',state=Evos_state.menu_burger)
async def burger_thing(message:types.Message):
    photo = open("Images/chizburger.jpg", "rb")
    await message.answer_photo(photo=photo, reply_markup=burgerassdf,caption="Narx: 24 000 so'm")

@dp.message_handler(text='Ortga qaytish 🔙', state=Evos_state.menu_burger)
async def menyu(message: types.Message, state: FSMContext):
    await message.answer('Tanlang:', reply_markup=menu)
    await state.finish()



#-------------------------Hot-Dog-------------------------#




@dp.message_handler(text='Hot-Dog (8)')
async def menyu(message:types.Message,state:FSMContext):
    photo = open("Images/hotdog2.jpg","rb")
    await message.answer_photo(photo=photo,reply_markup=hotgodsss)
    await Evos_state.menu_hotdog.set()



@dp.message_handler(text='Hot-dog baguette',state=Evos_state.menu_hotdog)
async def menyu(message:types.Message,state:FSMContext):
    photo = open("Images/oddiyhotdog.jpg","rb")
    await message.answer_photo(photo=photo,reply_markup=hotdog_button,caption="Narx: 14 000 so'm")




@dp.message_handler(text='Sub tovuq cheese',state=Evos_state.menu_hotdog)
async def menyu(message:types.Message,state:FSMContext):
    photo = open("Images/subtovuqcheese.jpg","rb")
    await message.answer_photo(photo=photo,reply_markup=hotdog_button,caption="Narx: 19 000 so'm")



@dp.message_handler(text='Sub tovuq',state=Evos_state.menu_hotdog)
async def menyu(message:types.Message,state:FSMContext):
    photo = open("Images/subtovuq.jpg","rb")
    await message.answer_photo(photo=photo,reply_markup=hotdog_button,caption="Narx: 17 000 so'm")



@dp.message_handler(text="Hot-dog baguette double",state=Evos_state.menu_hotdog)
async def menyu(message:types.Message,state:FSMContext):
    photo = open("Images/hotdogdouble.jpg","rb")
    await message.answer_photo(photo=photo,reply_markup=hotdog_button,caption="Narx: 21 000 so'm")



@dp.message_handler(text="Hot-dog kids",state=Evos_state.menu_hotdog)
async def menyu(message:types.Message,state:FSMContext):
    photo = open("Images/hotdogkids.jpg","rb")
    await message.answer_photo(photo=photo,reply_markup=hotdog_button,caption="Narx: 8 000 so'm")



@dp.message_handler(text="Sub go'sht cheese",state=Evos_state.menu_hotdog)
async def menyu(message:types.Message,state:FSMContext):
    photo = open("Images/subcheese.jpg","rb")
    await message.answer_photo(photo=photo,reply_markup=hotdog_button,caption="Narx: 21 000 so'm")




@dp.message_handler(text="Hot-dog classic",state=Evos_state.menu_hotdog)
async def menyu(message:types.Message,state:FSMContext):
    photo = open("Images/hotdogclassic.jpg","rb")
    await message.answer_photo(photo=photo,reply_markup=hotdog_button,caption="Narx: 8 000 so'm")





@dp.message_handler(text="Sub go'sht",state=Evos_state.menu_hotdog)
async def menyu(message:types.Message,state:FSMContext):
    photo = open("Images/subgoshttt.jpg","rb")
    await message.answer_photo(photo=photo,reply_markup=hotdog_button,caption="Narx: 19 000 so'm")



@dp.message_handler(text='Ortga qaytish 🔙', state=Evos_state.menu_hotdog)
async def menyu(message: types.Message, state: FSMContext):
    await message.answer('Tanlang:', reply_markup=menu)
    await state.finish()


#-------------------------ichimliklar-------------------------#



@dp.message_handler(text='Ichimliklar (11)',)
async def ichimliklar(message:types.Message,state:FSMContext):
    photo = open("Images/ichimliklar.jpg","rb")
    await message.answer_photo(photo=photo,reply_markup=ichimliklarr)
    await Evos_state.menu_ichimliklar.set()

@dp.message_handler(text='Sok dena 0,33l', state=Evos_state.menu_ichimliklar)
async def menyu(message: types.Message, state: FSMContext):
    photo = open("Images/sokdena.jpg", "rb")
    await message.answer_photo(photo=photo ,reply_markup=ichimliklar_button,caption="Narx: 10 000 so'm")


@dp.message_handler(text='Suv 0,5', state=Evos_state.menu_ichimliklar)
async def menyu(message: types.Message, state: FSMContext):
    photo = open("Images/suv05.jpg", "rb")
    await message.answer_photo(photo=photo ,reply_markup=ichimliklar_button,caption="Narx: 4 000 so'm")



@dp.message_handler(text='Pepsi 0,5', state=Evos_state.menu_ichimliklar)
async def menyu(message: types.Message, state: FSMContext):
    photo = open("Images/pepsi05.jpg", "rb")
    await message.answer_photo(photo=photo ,reply_markup=ichimliklar_button,caption="Narx: 9 000 so'm")



@dp.message_handler(text='Pepsi 1,5', state=Evos_state.menu_ichimliklar)
async def menyu(message: types.Message, state: FSMContext):
    photo = open("Images/pepsi15.jpg", "rb")
    await message.answer_photo(photo=photo ,reply_markup=ichimliklar_button,caption="Narx: 17 000 so'm")


@dp.message_handler(text='Quyib beriladigan Pepsi', state=Evos_state.menu_ichimliklar)
async def menyu(message: types.Message, state: FSMContext):
    photo = open("Images/pepsi04.jpg", "rb")
    await message.answer_photo(photo=photo ,reply_markup=ichimliklar_button,caption="Narx: 8 000 so'm")



@dp.message_handler(text='Bliss sharbati', state=Evos_state.menu_ichimliklar)
async def menyu(message: types.Message, state: FSMContext):
    photo = open("Images/bliss.jpg", "rb")
    await message.answer_photo(photo=photo ,reply_markup=ichimliklar_button,caption="Narx: 16 000 so'm")



@dp.message_handler(text='Amerikano', state=Evos_state.menu_ichimliklar)
async def menyu(message: types.Message, state: FSMContext):
    photo = open("Images/amerikano.jpg", "rb")
    await message.answer_photo(photo=photo ,reply_markup=ichimliklar_button,caption="Narx: 11 000 so'm")



@dp.message_handler(text='Latte', state=Evos_state.menu_ichimliklar)
async def menyu(message: types.Message, state: FSMContext):
    photo = open("Images/latte.jpg", "rb")
    await message.answer_photo(photo=photo ,reply_markup=ichimliklar_button,caption="Narx: 13 000 so'm")



@dp.message_handler(text="Ko'k choy", state=Evos_state.menu_ichimliklar)
async def menyu(message: types.Message, state: FSMContext):
    photo = open("Images/kokchoy.jpg", "rb")
    await message.answer_photo(photo=photo ,reply_markup=ichimliklar_button,caption="Narx: 4 000 so'm")




@dp.message_handler(text="Qora choy", state=Evos_state.menu_ichimliklar)
async def menyu(message: types.Message, state: FSMContext):
    photo = open("Images/qorachoy.jpg", "rb")
    await message.answer_photo(photo=photo ,reply_markup=ichimliklar_button,caption="Narx: 4 000 so'm")




@dp.message_handler(text="Limonli ko'k choy", state=Evos_state.menu_ichimliklar)
async def menyu(message: types.Message, state: FSMContext):
    photo = open("Images/limonli.jpg", "rb")
    await message.answer_photo(photo=photo ,reply_markup=ichimliklar_button,caption="Narx: 5 000 so'm")



@dp.message_handler(text='Ortga qaytish 🔙', state=Evos_state.menu_ichimliklar)
async def menyu(message: types.Message, state: FSMContext):
    await message.answer('Tanlang:', reply_markup=menu)
    await state.finish()




#-------------------------Shirinliklar va desertlar-------------------------#


@dp.message_handler(text="Shirinliklar va desertlar (4)")
async def shirinliklar(message:types.Message):
    photo = open("Images/.jpg", "rb")
    await message.answer_photo(photo=photo, reply_markup=ichimliklar_button)












if __name__ == '__main__':
    from plus_minus import dp, bot
    executor.start_polling(dp, skip_updates=True)
