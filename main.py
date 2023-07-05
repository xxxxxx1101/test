from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.utils import executor
from confing import TOKEN
from databoaes.db_file import databoase
from keyboards.db import get_keybord
from hendlers.sisi import Reqistration 
from bot1212bs  import  dp
bot = Bot(token=TOKEN)



@dp.message_handler(commands='start')
async def start_command(message: Message):
    db = databoase()
    db.connect()
    db.create_user_table()
    user_id = message.from_user.id
    check_users = db.check_user(user_id)
    if check_users:
        await message.answer('Привет ты зарегистрирован', reply_markup=get_keybord('start_menu'))
    else:
        registration = Reqistration(message)
        await registration.registration_user(message)
    db.close()

@dp.message_handler(text='Товары')
async def product_hendler(message:Message):
    pass

@dp.message_handler(text='Корзина')
async def  cart_hendler(message:Message):
    pass
@dp.message_handler(text= 'Личный Кабинет')
async def privat_office_hendler(message:Message):
    pass
@dp.message_handler(text= 'Тех.поддержка')
async def privat_office_hendler(message:Message):
    pass

if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)
