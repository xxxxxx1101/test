from aiogram import Bot,Dispatcher
from confing  import TOKEN 
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor


bot = Bot(token=TOKEN)
dp = Dispatcher(bot,storage=MemoryStorage())


if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)