import logging
from aiogram import executor
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from Keyboards.default import *
from Keyboards.inline import *
from config import API_TOKEN
import sqlite3






from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())

conn = sqlite3.connect('stats.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS stats
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   user_id INTEGER,
                   date DATE)''')
conn.commit()

def record_stat(user_id):
    cursor.execute("INSERT INTO stats (user_id, date) VALUES (?, DATE('now'))", (user_id,))
    conn.commit()


@dp.message_handler(commands=['stats'])
async def show_stats(message: types.Message):
    cursor.execute("SELECT COUNT(DISTINCT user_id) FROM stats")
    total_users = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(DISTINCT user_id) FROM stats WHERE date = DATE('now')")
    today_users = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM stats")
    total_requests = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM stats WHERE date = DATE('now')")
    today_requests = cursor.fetchone()[0]

    text = f"📊 Botdan foydalanish statistikasi:\n" \
           f" ├ Jami foydalanuvchilar: {total_users}\n" \
           f" ├ Bugungi foydalanuvchilar: {today_users}\n" \
           f" ├ Jami so'rovlar: {total_requests}\n" \
           f" └ Bugungi so'rovlar: {today_requests}"

    await message.reply(text)


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
    menu_shirinliklar = State()
    menu_garnirlar = State()
    xabar_yubormoq = State()
    settingsss = State()
    buyurtma_berish = State()


son = {
    'user_id': 1
}




#-------------------------Start-------------------------#
@dp.message_handler(commands='start')
async def command1(message: types.Message, state: FSMContext):
    #check database HAVE BEEN USER_ID
    cursor.execute("SELECT user_id FROM stats WHERE user_id = ?", (message.from_user.id,))
    user_id = cursor.fetchone()
    record_stat(message.from_user.id)
    await message.answer('<b>EVOS | Доставка</b> botiga xush kelibsiz!', reply_markup=number_p)
    await message.answer('''
Avval telefon raqamingizni yuboring,
yoki <b>+998XX XXXXXXX</b> ko'rinishida yozing.

<a href="https://evos.uz/uz/about/">Evos</a>    
        ''', reply_markup=number_p)
    await Evos_state.phone_number.set()
    await record_stat(message.from_user.id)




@dp.message_handler(content_types=types.ContentType.CONTACT, state=Evos_state.phone_number)
async def phone_number(message: types.Message, state: FSMContext):
    await message.answer('<b>Iltimos joylashuvni yuboring!</b>', reply_markup=location)
    await state.finish()
    await Evos_state.location.set()


@dp.message_handler(content_types=types.ContentType.LOCATION, state=Evos_state.location)
async def user_location(message: types.Message, state: FSMContext):
    await message.answer('<b>EVOS | Доставка</b>botiga xush kelibsiz!', reply_markup=all_buttons)
    await state.finish()


@dp.message_handler(text='Menu 🍴')
async def menyu(message: types.Message, state: FSMContext):
    await message.answer('Tanlang:', reply_markup=menu)

#-------------------------Setlar-------------------------#


@dp.message_handler(text='Setlar (8)')
async def menusetlar(message: types.Message, state: FSMContext):
    photo = open('Images/setlar-menu.jpg', 'rb')
    await message.answer_photo(photo=photo, reply_markup=menusetlarrr)



@dp.message_handler(text='Combo Plus Isituvchan (Qora choy)')
async def qora_choy(message: types.Message):
    son[message.from_user.id] = 1
    photo = open('Images/qorachoy+.jpg', 'rb')
    await message.answer_photo(photo=photo, reply_markup=comboqorachoy, caption="Narxi: 16 000 so'm")

@dp.message_handler(text='FitCombo')
async def fitcombooooo(message:types.Message):
    son[message.from_user.id] = 1
    photo = open('Images/fitcombo.jpg', 'rb')
    await message.answer_photo(photo=photo, reply_markup=fitcombooo, caption="Narxi: 30 000 so'm")

@dp.message_handler(text="Iftar kofte grill mol go'shtidan")
async def iftarkofte(message:types.Message):
    son[message.from_user.id] = 1
    photo = open('Images/iftarkofte.jpg', 'rb')
    await message.answer_photo(photo=photo, reply_markup=iftarkoftegrill, caption='''
Muborak RAMAZON oyi munosabati
bilan maxsus taklif! Mol go'shtli 
5 dona shirali gril-kotletlari, guruch, 
limon sharbati bilan boyitilgan qizil karamli 
salat, pomidorlar va yong'oqlardan tayyorlangan 
maxsus quyuq RAMAZON sousi. Iftorlik 
vaqtingiz uchun ideal yechim!
Narxi: 35 000 so'm    
    ''',)
@dp.message_handler(text="Donar boks  mol go'shtidan")
async def donarboks(message:types.Message):
    son[message.from_user.id] = 1
    photo = open('Images/donarboks.jpg', 'rb')
    await message.answer_photo(photo=photo, reply_markup=donarmol, caption='''
YANGILIK! Oq kunjut sousi ostidagi shirali grill tovuq go'shti, qarsildoq kartoshka-fri, donador guruch, qizil karamdan tayyorlangan barra salatdan tashkil topgan qatlamlarning to'yimli uyg'unlashuvi. Qulay, ixcham, ammo to'yimli qadoq!
Narxi: 34 000 so'm    
    ''')

@dp.message_handler(text="COMBO+")
async def donarboks(message:types.Message, ):
    son[message.from_user.id] = 1
    photo = open('Images/com+bo.jpg', 'rb')
    await message.answer_photo(photo=photo, reply_markup=com_bo,caption='''
Yeng yaxshi taklif! Issiq qarsildoq qovurilgan kartoshka va bir stakan Pepsi
Narxi: 16 000 so'm    
    ''')


@dp.message_handler(text="Donar boks tovuq go'shtidan")
async def donarboks(message:types.Message):
    son[message.from_user.id] = 1
    photo = open('Images/donartovuq.jpg', 'rb')
    await message.answer_photo(photo=photo, reply_markup=donarbokstovuq, caption='''
YANGILIK!  Yangi, maxsus tayyorlangan teriyaki sousi, grill tovuq go'shti, qarsildoq kartoshka-fri, donador guruch, limon sharbati bilan to'yintirilgan qizil karamdan tayyorlangan barra salatning noodatiy mazali uyg'unlashuvi. Qulay, ixcham, ammo to'yimli qadoq!
Narxi: 32 000 so'm
    ''')



@dp.message_handler(text="Iftar strips tovuq go'shtidan")
async def donarboks(message:types.Message):
    son[message.from_user.id] = 1
    photo = open('Images/iftartovuq.jpg', 'rb')
    await message.answer_photo(photo=photo, reply_markup=iftartovuqgosht, caption='''
Muborak RAMAZON oyi munosabati bilan maxsus taklif! Tovuqli 5 dona shirali gril-kotletlari, guruch, limon sharbati bilan boyitilgan qizil karamli salat, pomidorlar va yong'oqlardan tayyorlangan maxsus quyuq RAMAZON sousi. Iftorlik vaqtingiz uchun ideal yechim!
Narxi: 30 000 so'm
    ''')

@dp.message_handler(text="Kids COMBO")
async def donarboks(message:types.Message):
    son[message.from_user.id] = 1
    photo = open('Images/kidscombo.jpg', 'rb')
    await message.answer_photo(photo=photo, reply_markup=kidscombo, caption='''
Narxi: 16 000 so'm
    ''')

@dp.message_handler(text='Orqaga qaytish 🔙')
async def menyu(message: types.Message, state: FSMContext):
    await message.answer('Tanlang:', reply_markup=menu)
    await state.finish()


@dp.message_handler(text='Orqaga qaytish🔙')
async def menyu(message: types.Message, state: FSMContext):
    await message.answer('Tanlang:', reply_markup=all_buttons)


#----------------------Lavash----------------------#



@dp.message_handler(text='Lavash (9)')
async def lavashalar(message:types.Message,state:FSMContext):
    photo = open('Images/lavashs.jpg', 'rb')
    await message.answer_photo(photo=photo, reply_markup=lavashssss)




@dp.message_handler(text='Mol goʼshtidan qalampir lavash',)
async def lavashlar(message:types.Message):
    son[message.from_user.id] = 1
    photo = open('Images/qalampirlavash.jpg', 'rb')
    await message.answer_photo(photo=photo, reply_markup=lavash2,caption='''
Qarsildoq chipslar, yangi bodring va pomidorlar bilan lavashga oʼralgan yumshoq mol goʼshti, bizning taʼmi oʼtkir qayla bilan
Narxi: 26 000 so'm    
    ''')

@dp.message_handler(text='Tovuq goʼshtli qalampir lavash',)
async def lavashlar(message:types.Message):
    son[message.from_user.id] = 1
    photo = open('Images/goshtgalampir.jpg', 'rb')
    await message.answer_photo(photo=photo, reply_markup=qalampirlavash,caption='''
Yangi bodring va pomidorlar, qarsildoq chipslar bilan lavashga oʼralgan qovurilgan tovuq filesi, bizning taʼmi oʼtkir maxsus qayla bilan
Narxi: 24 000 so'm    
    ''')

@dp.message_handler(text='Mol goʼshtidan pishloqli lavash Standard',)
async def lavashlar(message:types.Message):
    son[message.from_user.id] = 1
    photo = open('Images/lavashstandard.jpg', 'rb')
    await message.answer_photo(photo=photo,reply_markup=mmolgoshtstandard, caption='Narx: 22 000 soʼm')



@dp.message_handler(text="Lavash cheese tovuq go'sht Standart",)
async def mini(message:types.Message):
    son[message.from_user.id] = 1
    photo = open('Images/cheesetovuq.jpg', 'rb')
    await message.answer_photo(photo=photo,reply_markup=standardcheese,caption="Narx: 27 000 so'm" )

@dp.message_handler(text='FITTER',)
async def lavashlar(message:types.Message):
    son[message.from_user.id] = 1
    photo = open('Images/fitter.jpg', 'rb')
    await message.answer_photo(photo=photo, reply_markup=fitter, caption='''
Tovuq goʼshti, qarsildoq muztogʼ salati, yangi bodring va pomidorlar, fetaksa va bizning maxsus qaylamiz - barchasi yashil lavashga oʼralgan
Narxi: 22 000 so'm    
    ''')

@dp.message_handler(text="Lavash tovuq go'sht",)
async def mini(message:types.Message):
    son[message.from_user.id] = 1
    photo = open('Images/tovuqgoshtbigmin.jpg', 'rb')
    await message.answer_photo(photo=photo, reply_markup=tovuqgosht,caption="Narx: 22 000 so'm" )



@dp.message_handler(text='Orqaga qaytish 🔙',)
async def menyu(message: types.Message, state: FSMContext):
    son[message.from_user.id] = 1
    await message.answer('Tanlang:', reply_markup=menu)
    await state.finish()

#----------------------shaurma----------------------#




@dp.message_handler(text='Shaurma (4)')
async def shaurmaaa(message:types.Message,state:FSMContext):
    son[message.from_user.id] = 1
    photo = open('Images/shaurma.jpg', 'rb')
    await message.answer_photo(photo=photo, reply_markup=shaurma)


@dp.message_handler(text="Shaurma tovuq go'sht",)
async def shaurmaadsgasd(message:types.Message):
    son[message.from_user.id] = 1
    photo = open('Images/shurma2.jpg', 'rb')
    await message.answer_photo(photo=photo,reply_markup=shaurmatovuqg ,caption="Narx: 24 000 so'm")

@dp.message_handler(text="Shaurma qalampir mol go'sht",)
async def shaurmassasd(message:types.Message,state:FSMContext):
    son[message.from_user.id] = 1
    photo = open('Images/shurma.jpg', 'rb')
    await message.answer_photo(photo=photo,reply_markup=qmolgosht,caption="Narx: 22 000 so'm")

@dp.message_handler(text="Shaurma qalampir tovuq go'sht")
async def shaurmasdgasa(message:types.Message,state:FSMContext):
    son[message.from_user.id] = 1
    photo = open('Images/shurma2.jpg', 'rb')
    await message.answer_photo(photo=photo,reply_markup=qtovuqgosht,caption="Narx: 26 000 so'm")

@dp.message_handler(text="Shaurma mol go'sht")
async def shauasdgasdrma(message:types.Message,state:FSMContext):
    son[message.from_user.id] = 1
    photo = open('Images/shurma.jpg', 'rb')
    await message.answer_photo(photo=photo, reply_markup=shmolgosht,caption="Narx: 24 000 so'm")

@dp.message_handler(text="Ortga qaytish 🔙")
async def menyu(message: types.Message, state: FSMContext):
    await message.answer('Tanlang:', reply_markup=menu)
    await state.finish()


#-------------------------Burger-------------------------#

@dp.message_handler(text="Burger (4)")
async def burger(message:types.Message,state:FSMContext):
    son[message.from_user.id] = 1
    photo = open("Images/burgers.jpg","rb")
    await message.answer_photo(photo=photo,reply_markup=burgerss)



@dp.message_handler(text='Gamburger')
async def burger_thing(message:types.Message):
    son[message.from_user.id] = 1
    photo = open("Images/gamburger.jpg", "rb")
    await message.answer_photo(photo=photo, reply_markup=gamburger,caption="Narx: 22 000 so'm")

@dp.message_handler(text='Double burger')
async def burger_thing(message:types.Message):
    son[message.from_user.id] = 1
    photo = open("Images/doubleburger.jpg", "rb")
    await message.answer_photo(photo=photo, reply_markup=doubleburgere,caption="Narx: 33 000 so'm")


@dp.message_handler(text='Double cheese')
async def burger_thing(message:types.Message):
    son[message.from_user.id] = 1
    photo = open("Images/dcheeseburger.jpg", "rb")
    await message.answer_photo(photo=photo, reply_markup=doublecheese,caption="Narx: 37 000 so'm")
@dp.message_handler(text='Cheese burger')
async def burger_thing(message:types.Message):
    son[message.from_user.id] = 1
    photo = open("Images/chizburger.jpg", "rb")
    await message.answer_photo(photo=photo, reply_markup=cheeseburger,caption="Narx: 24 000 so'm")

@dp.message_handler(text='Ortga qaytish 🔙')
async def menyu(message: types.Message, state: FSMContext):
    son[message.from_user.id] = 1
    await message.answer('Tanlang:', reply_markup=menu)
    await state.finish()



#-------------------------Hot-Dog-------------------------#




@dp.message_handler(text='Hot-Dog (8)')
async def menyu(message:types.Message,state:FSMContext):
    photo = open("Images/hotdog2.jpg","rb")
    await message.answer_photo(photo=photo,reply_markup=hotgodsss)




@dp.message_handler(text='Hot-dog baguette')
async def menyu(message:types.Message,state:FSMContext):
    son[message.from_user.id] = 1
    photo = open("Images/oddiyhotdog.jpg","rb")
    await message.answer_photo(photo=photo,reply_markup=hotdogbagguate,caption="Narx: 14 000 so'm")




@dp.message_handler(text='Sub tovuq cheese')
async def menyu(message:types.Message,state:FSMContext):
    son[message.from_user.id] = 1
    photo = open("Images/subtovuqcheese.jpg","rb")
    await message.answer_photo(photo=photo,reply_markup=subtovuqcheese,caption="Narx: 19 000 so'm")



@dp.message_handler(text='Sub tovuq')
async def menyu(message:types.Message,state:FSMContext):
    son[message.from_user.id] = 1
    photo = open("Images/subtovuq.jpg","rb")
    await message.answer_photo(photo=photo,reply_markup=subtovuq,caption="Narx: 17 000 so'm")



@dp.message_handler(text="Hot-dog baguette double")
async def menyu(message:types.Message,state:FSMContext):
    son[message.from_user.id] = 1
    photo = open("Images/hotdogdouble.jpg","rb")
    await message.answer_photo(photo=photo,reply_markup=hotdogbagguated,caption="Narx: 21 000 so'm")



@dp.message_handler(text="Hot-dog kids")
async def menyu(message:types.Message,state:FSMContext):
    son[message.from_user.id] = 1
    photo = open("Images/hotdogkids.jpg","rb")
    await message.answer_photo(photo=photo,reply_markup=hotdogkids,caption="Narx: 8 000 so'm")



@dp.message_handler(text="Sub go'sht cheese")
async def menyu(message:types.Message,state:FSMContext):
    son[message.from_user.id] = 1
    photo = open("Images/subcheese.jpg","rb")
    await message.answer_photo(photo=photo,reply_markup=subgoshtcheese,caption="Narx: 21 000 so'm")




@dp.message_handler(text="Hot-dog classic")
async def menyu(message:types.Message,state:FSMContext):
    son[message.from_user.id] = 1
    photo = open("Images/hotdogclassic.jpg","rb")
    await message.answer_photo(photo=photo,reply_markup=hotdogclasic,caption="Narx: 8 000 so'm")





@dp.message_handler(text="Sub go'sht")
async def menyu(message:types.Message,state:FSMContext):
    son[message.from_user.id] = 1
    photo = open("Images/subgoshttt.jpg","rb")
    await message.answer_photo(photo=photo,reply_markup=subgosht,caption="Narx: 19 000 so'm")



@dp.message_handler(text='Ortga qaytish 🔙',)
async def menyu(message: types.Message, state: FSMContext):
    await message.answer('Tanlang:', reply_markup=menu)
    await state.finish()


#-------------------------ichimliklar-------------------------#



@dp.message_handler(text='Ichimliklar (11)',)
async def ichimliklar(message:types.Message,state:FSMContext):
    photo = open("Images/ichimliklar.jpg","rb")
    await message.answer_photo(photo=photo,reply_markup=ichimliklarr)


@dp.message_handler(text='Sok dena 0,33l')
async def menyu(message: types.Message, state: FSMContext):
    photo = open("Images/sokdena.jpg", "rb")
    await message.answer_photo(photo=photo ,reply_markup=sokdena,caption="Narx: 10 000 so'm")


@dp.message_handler(text='Suv 0,5')
async def menyu(message: types.Message, state: FSMContext):
    photo = open("Images/suv05.jpg", "rb")
    await message.answer_photo(photo=photo ,reply_markup=suv05,caption="Narx: 4 000 so'm")



@dp.message_handler(text='Pepsi 0,5')
async def menyu(message: types.Message, state: FSMContext):
    photo = open("Images/pepsi05.jpg", "rb")
    await message.answer_photo(photo=photo ,reply_markup=pepsi05,caption="Narx: 9 000 so'm")



@dp.message_handler(text='Pepsi 1,5')
async def menyu(message: types.Message, state: FSMContext):
    photo = open("Images/pepsi15.jpg", "rb")
    await message.answer_photo(photo=photo ,reply_markup=pepsi15,caption="Narx: 17 000 so'm")


@dp.message_handler(text='Quyib beriladigan Pepsi')
async def menyu(message: types.Message, state: FSMContext):
    photo = open("Images/pepsi04.jpg", "rb")
    await message.answer_photo(photo=photo ,reply_markup=quyibpepsi,caption="Narx: 8 000 so'm")



@dp.message_handler(text='Bliss sharbati')
async def menyu(message: types.Message, state: FSMContext):
    photo = open("Images/bliss.jpg", "rb")
    await message.answer_photo(photo=photo ,reply_markup=blisharbat,caption="Narx: 16 000 so'm")



@dp.message_handler(text='Amerikano')
async def menyu(message: types.Message, state: FSMContext):
    photo = open("Images/amerikano.jpg", "rb")
    await message.answer_photo(photo=photo ,reply_markup=Amerikano,caption="Narx: 11 000 so'm")



@dp.message_handler(text='Latte')
async def menyu(message: types.Message, state: FSMContext):
    photo = open("Images/latte.jpg", "rb")
    await message.answer_photo(photo=photo ,reply_markup=lattle,caption="Narx: 13 000 so'm")



@dp.message_handler(text="Ko'k choy")
async def menyu(message: types.Message, state: FSMContext):
    photo = open("Images/kokchoy.jpg", "rb")
    await message.answer_photo(photo=photo ,reply_markup=kokchoy,caption="Narx: 4 000 so'm")




@dp.message_handler(text="Qora choy")
async def menyu(message: types.Message, state: FSMContext):
    photo = open("Images/qorachoy.jpg", "rb")
    await message.answer_photo(photo=photo ,reply_markup=qorachoyo,caption="Narx: 4 000 so'm")




@dp.message_handler(text="Limonli ko'k choy")
async def menyu(message: types.Message, state: FSMContext):
    photo = open("Images/limonli.jpg", "rb")
    await message.answer_photo(photo=photo ,reply_markup=limonchoy,caption="Narx: 5 000 so'm")



@dp.message_handler(text='Ortga qaytish 🔙')
async def menyu(message: types.Message, state: FSMContext):
    await message.answer('Tanlang:', reply_markup=menu)
    await state.finish()




#-------------------------Shirinliklar va desertlar-------------------------#


@dp.message_handler(text="Shirinliklar va desertlar (4)")
async def shirinliklar(message:types.Message,state:FSMContext):
    photo = open("Images/shirinliklar.jpg", "rb")
    await message.answer_photo(photo=photo, reply_markup=shirinliklar_button)





@dp.message_handler(text="Medovik Asalim")
async def shirinliklar(message:types.Message):
    photo = open("Images/medovek.jpg", "rb")
    await message.answer_photo(photo=photo, reply_markup=asalim,caption="Narx: 16 000 so'm")

@dp.message_handler(text="Chizkeyk")
async def shirinliklar(message:types.Message):
    photo = open("Images/chizkeyk.jpg", "rb")
    await message.answer_photo(photo=photo, reply_markup=chizkeyk,caption="Narx: 16 000 so'm")






@dp.message_handler(text="Donut karameli")
async def shirinliklar(message:types.Message):
    photo = open("Images/karamelniy.jpg", "rb")
    await message.answer_photo(photo=photo, reply_markup=karamelin,caption="Narx: 15 000 so'm")



@dp.message_handler(text="Donut mevali")
async def shirinliklar(message:types.Message):
    photo = open("Images/donutmevali.jpg", "rb")
    await message.answer_photo(photo=photo, reply_markup=mevali,caption="Narx: 15 000 so'm")


@dp.message_handler(text='Ortga qaytish 🔙',)
async def menyu(message: types.Message, state: FSMContext):
    await message.answer('Tanlang:', reply_markup=menu)
    await state.finish()

#-----garnirlar-----#

@dp.message_handler(text='Garnirlar (10)')
async def garnirlar1(message:types.Message,state:FSMContext):
    photo = open("Images/garnirlar.jpg", "rb")
    await message.answer_photo(photo=photo,reply_markup=garnirlar)




@dp.message_handler(text='Ketchup')
async def garnirlar1(message:types.Message,state:FSMContext):
    photo = open("Images/ketchup.jpg", "rb")
    await message.answer_photo(photo=photo,reply_markup=ketchup,caption="Narx: 2 000 so'm")



@dp.message_handler(text='Guruch')
async def ketsh(message:types.Message):
    photo = open("Images/guruch.jpg", "rb")
    await message.answer_photo(photo=photo, reply_markup=guruch, caption="Narx: 7  000 so'm")



@dp.message_handler(text='Tovuq Strips')
async def ketsh(message:types.Message):
    photo = open("Images/tovuqstrips.jpg", "rb")
    await message.answer_photo(photo=photo,reply_markup=tovuqstrips, caption="Narx: 19 000 so'm")


@dp.message_handler(text='Pishloqli sous')
async def pishloqsous(message:types.Message):
    photo = open("Images/pishloqsous.jpg", "rb")
    await message.answer_photo(photo=photo, reply_markup=pishloqli_sous, caption="Narx: 2 000 so'm")

@dp.message_handler(text='Chisnokli sous')
async def pishloqsous(message:types.Message):
    photo = open("Images/chisnoksous.jpg", "rb")
    await message.answer_photo(photo=photo, reply_markup=chisnokli_sous, caption="Narx: 2 000 so'm")

@dp.message_handler(text='Chili sous')
async def pishloqsous(message:types.Message):
    photo = open("Images/chilisous.jpg", "rb")
    await message.answer_photo(photo=photo, reply_markup=chilisous, caption="Narx: 2 000 so'm")


from Keyboards.inline import chilisous, barbekusous, salat
@dp.message_handler(text='Barbekyu sousi')
async def pishloqsous(message:types.Message):
    photo = open("Images/barbekusous.jpg", "rb")
    await message.answer_photo(photo=photo, reply_markup=barbekusous, caption="Narx: 2 000 so'm")


@dp.message_handler(text='Salat')
async def pishloqsous(message:types.Message):
    photo = open("Images/salat.jpg", "rb")
    await message.answer_photo(photo=photo, reply_markup=salat, caption="Narx: 7 000 so'm")



@dp.message_handler(text='Non')
async def pishloqsous(message:types.Message):
    photo = open("Images/non.jpg", "rb")
    await message.answer_photo(photo=photo, reply_markup=non, caption="Narx: 3 000 so'm")


@dp.message_handler(text='Fri')
async def pishloqsous(message:types.Message):
    photo = open("Images/fri.jpg", "rb")
    await message.answer_photo(photo=photo, reply_markup=fri, caption="Narx: 14 000 so'm")




@dp.message_handler(text='Orqaga qaytish 🔙')
async def manuyu(message:types.Message):
    await message.answer('<b>EVOS | Доставка</b>botiga xush kelibsiz!',reply_markup=all_buttons)





@dp.message_handler(text='Ortga qaytish')
async def menyu(message: types.Message, state: FSMContext):
    son[message.from_user.id] = 1
    await message.answer('Tanlang:', reply_markup=all_buttons)
    await state.finish()


#-------------------------Aloqa 📞-------------------------#

@dp.message_handler(text='Aloqa 📞')
async def aloqa(message:types.Message):
    photo = open("Images/aloqa.jpg", "rb")
    await message.answer_photo(photo=photo,caption='''
<b>Kontaktlar</b>
<b>Call-центр</b>

+998 71-203-12-12
+998 71-203-55-55
<b>Yetkazib berish telefon raqamlar:</b>

Toshkent
+998 71-203-12-12
Namangan
+998 78-147-12-12
Farg`ona
+998 73-249-12-12
Qo`qon
+998 73-542-78-78
Andijon
+998 74-224-12-12
Samarqand
+998 78-129-16-16
Qarshi
+998 78-129-17-17
    ''')

@dp.message_handler(text='Xabar yuborish 📨')
async def sendmessage(message:types.Message,state:FSMContext):
    await message.answer('Xabaringizni yozing:')
    await Evos_state.xabar_yubormoq.set()



@dp.message_handler(state=Evos_state.xabar_yubormoq)
async def getmessage(message:types.Message,state:FSMContext):
    text = message.text
    await message.answer("<b>Xabaringiz yuborildi</b>")
    await message.answer("Tez orada sizga aloqaga chiqishadi")
    await bot.send_message( 6498877955,f" {message.from_user.full_name}: {text}")
    await state.finish()


@dp.message_handler(text='Biz haqimizda ℹ️')
async def bizhaqimizda(message:types.Message):
    photo = open("Images/evos.jpg","rb")
    await message.answer_photo(photo=photo,caption='''
<b>Kompaniyamizning birinchi filiali 2006 yilda ochilgan bo’lib, shu kungacha muvaffaqiyatli faoliyat yuritib kelmoqdaligini bilarmidingiz?</b>15 yil davomida kompaniya avtobus bekatidagi kichik ovqatlanish joyidan zamonaviy, kengaytirilgan tarmoqqa aylandi, u bugungi kunda O‘zbekiston bo‘ylab 60 dan ortiq restoranlarni, o‘zining eng tezkor yetkazib berish xizmatini, zamonaviy IT-infratuzilmasini va 2000 dan ortiq xodimlarni o‘z ichiga oladi.

<a href="https://evos.uz/uz/about/">Evos</a>
    ''')


@dp.message_handler(text='Sozlamalar ⚙️',)
async def setttings(message:types.Message,state:FSMContext):
    await message.answer("<b>📋 | Sozlamalar bo'limiga xush kelibsiz!</b>",reply_markup=settings)
    await Evos_state.settingsss.set()

@dp.message_handler(text='Malumotlarni ochirib yuborish 🗑️',state=Evos_state.settingsss)
async def til(message:types.Message,state:FSMContext):
    c.execute(f"DELETE FROM savatcha WHERE user_id = {message.chat.id}")
    await message.answer('<b>Malumotlaringiz tozalandi</b>')
    await message.answer('/start ni bosib botni qayta ishga tushuring.')
    await state.finish()
#
@dp.message_handler(text='Orqaga qaytish 🔙',state=Evos_state.settingsss)
async def tilasdg(message:types.Message,state:FSMContext):
    await message.answer("EVOS | Доставкаbotiga xush kelibsiz!",reply_markup=all_buttons)
    await state.finish()

#
#-------------------------MENING BUYURTMALARIM-------------------------#

@dp.message_handler(text='Mening buyurtmalarim 🍽️')
async def buyurtmalarim(message:types.Message):
    await message.answer("<b>📋 | Mening buyurtmalarim bo'limiga xush kelibsiz!\n\nSizning buyurtmalaringiz</b>")
    c.execute(f"SELECT * FROM savatcha WHERE user_id = {message.chat.id}")
    zakazlar = c.fetchall()
    if zakazlar:
        for i in zakazlar:
            await message.answer(f'{i[1]} - {i[2]} so\'m - {i[3]} ta')
    else:
        await message.answer('Savatcha bo\'sh')


if __name__ == '__main__':
    from plus_minus import dp
    from savatcha import dp,c
    from buyurtma_berish import dp
    executor.start_polling(dp, skip_updates=True)
