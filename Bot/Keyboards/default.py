from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

number_p = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Telefon raqamni yuborish 📞',request_contact=True)
        ]
    ],
    resize_keyboard=True
)

location = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Joylashuvni yuborish 📍',request_location=True)
        ]
    ],
    resize_keyboard=True
)

all_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Menu 🍴')
        ],
        [
            KeyboardButton('Mening buyurtmalarim 🍽️')
        ],
        [
            KeyboardButton('Savat 📥'),
            KeyboardButton('Aloqa 📞')
        ],
        [
            KeyboardButton('Xabar yuborish 📨'),
            KeyboardButton('Sozlamalar ⚙️')
        ],
        [
            KeyboardButton('Biz haqimizda ℹ️')
        ]
    ],
    resize_keyboard=True
)
menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Setlar (8)')
        ],
        [
            KeyboardButton('Lavash (9)'),
            KeyboardButton('Shaurma (4)')
        ],
        [
            KeyboardButton('Burger (4)'),
            KeyboardButton('Hot-Dog (8)')
        ],
        [
            KeyboardButton('Ichimliklar (11)')
        ],
        [
            KeyboardButton('Shirinliklar va desertlar (4)')
        ],
        [
            KeyboardButton('Garnirlar (10)')
        ],
        [
            KeyboardButton('Orqaga qaytish 🔙')
        ]
    ],
    resize_keyboard=True
)


menusetlarrr = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Combo Plus Isituvchan (Qora choy)'),
            KeyboardButton('FitCombo')
        ],
        [
            KeyboardButton("Iftar kofte grill mol go'shtidan"),
            KeyboardButton("Donar boks  mol go'shtidan")
        ],
        [
            KeyboardButton("Donar boks tovuq go'shtidan"),
            KeyboardButton("COMBO+")
        ],
        [
            KeyboardButton("Iftar strips tovuq go'shtidan"),
            KeyboardButton("Kids COMBO")
        ],
        [
            KeyboardButton("Orqaga qaytish 🔙"),
        ]

    ],
    resize_keyboard=True
)


lavashssss = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Mol goʼshtidan qalampir lavash"),
            KeyboardButton("Tovuq goʼshtli qalampir lavash")
        ],
        [
            KeyboardButton("Mol goʼshtidan pishloqli lavash Standard"),
            KeyboardButton("Lavash cheese tovuq go'sht Standart")
        ],
        [
            KeyboardButton("FITTER"),
            KeyboardButton("Lavash tovuq go'sht")
        ],
        [
            KeyboardButton("Orqaga qaytish 🔙")
        ]

    ],
    resize_keyboard=True
)

shaurma = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Shaurma qalampir mol go'sht"),
            KeyboardButton("Shaurma tovuq go'sht")
        ],
        [
            KeyboardButton("Shaurma qalampir tovuq go'sht"),
            KeyboardButton("Shaurma mol go'sht")
        ],
        [
            KeyboardButton("Ortga qaytish 🔙")
        ]
    ],
    resize_keyboard=True
)


burgerss = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Gamburger"),
            KeyboardButton("Double burger")
        ],
        [
            KeyboardButton("Cheese burger"),
            KeyboardButton("Double cheese")
        ],
        [
            KeyboardButton("Ortga qaytish 🔙")
        ]
    ],
    resize_keyboard=True
)
hotgodsss = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Hot-dog baguette"),
            KeyboardButton("Sub tovuq cheese")
        ],
        [
            KeyboardButton("Sub tovuq"),
            KeyboardButton("Hot-dog baguette double")
        ],
        [
            KeyboardButton("Hot-dog kids"),
            KeyboardButton("Sub go'sht cheese")
        ],
        [
            KeyboardButton("Hot-dog classic"),
            KeyboardButton("Sub go'sht")
        ],
        [
            KeyboardButton("Ortga qaytish 🔙")
        ]

    ],
    resize_keyboard=True
)


ichimliklarr = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Sok dena 0,33l"),
            KeyboardButton("Suv 0,5")
        ],
        [
            KeyboardButton("Pepsi 0,5"),
            KeyboardButton("Pepsi 1,5")
        ],
        [
            KeyboardButton("Quyib beriladigan Pepsi"),
            KeyboardButton("Bliss sharbati")
        ],
        [
            KeyboardButton("Amerikano"),
            KeyboardButton("Latte")
        ],
        [
            KeyboardButton("Ko'k choy"),
            KeyboardButton("Qora choy")
        ],
        [
            KeyboardButton("Limonli ko'k choy"),
        ],

        [
            KeyboardButton("Ortga qaytish 🔙")
        ]

    ],
    resize_keyboard=True
)






