from aiogram.dispatcher.filters.state import State,StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, Contact,KeyboardButton,ReplyKeyboardMarkup
from aiogram import types
from bot1212bs import bot,dp
from databoaes.db_file import databoase
from keyboards.db import get_keybord
from aiogram.utils import executor
class Reqistration:
    def __init__(self, message:Message):
        self.message=message




    async def registration_user(self, message:Message):
        class RegistrationState(StatesGroup):
            phone = State()



        await RegistrationState.phone.set()
        keyboar =  ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
        keyboar.add(KeyboardButton('Отправить номер телефона',request_contact=True))
        await message.answer('Введите номер телефона для регестрации',reply_markup=keyboar)


        @dp.message_handler(content_types=types.ContentType.CONTACT,state=RegistrationState.phone)
        async def phone_stete(message:Message,state: FSMContext):
            async with state.proxy() as data:
                data['phone'] = message.contact.phone_number
                phone=data['phone']
                await message.answer(f'Вот ваш номер телефона\n{phone}',reply_markup=get_keybord('start_menu'))
                db = databoase()
                db.connect()
                db.create_user_table()
                user_id = message.from_user.id
                first_name = message.from_user.first_name
                db.add_user(first_name, user_id, phone)
                db.close()
                await state.finish()


if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)
