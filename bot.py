
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from database import SessionLocal, engine
from models import Base
from handlers import user_handlers, training_handlers
from dotenv import load_dotenv

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Загружаем переменные из .env файла
load_dotenv()

# Получаем API_TOKEN из окружения
API_TOKEN = os.getenv("API_TOKEN")

# Создание базы данных
Base.metadata.create_all(bind=engine)

# Создание бота и диспетчера
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Регистрация обработчиков
# user_handlers.register_handlers(dp)
# training_handlers.register_handlers(dp)

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
