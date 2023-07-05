from aiogram.types import KeyboardButton,ReplyKeyboardMarkup


def get_keybord(name:str):
    if name == 'start_menu':
        ketbord = ReplyKeyboardMarkup(resize_keyboard=True)
        ketbord.add(KeyboardButton('Товары'),('Корзина'))
        ketbord.add(KeyboardButton('Личный кабинет'),('Тех.поддержка'))
    elif name == 'test':
        ketbord = ReplyKeyboardMarkup(resize_keyboard=True)
        ketbord.add(KeyboardButton('test1'),('test2'))
     
    


    return ketbord