import asyncio
import logging
import limited_aiogram

from aiogram import Dispatcher

from app.handlers import handlers, chat_hendlers
from config_data.config import ConfigEnv, load_config

# Инициализируем логгер
logger = logging.getLogger(__name__)

# Загружаем конфиг в переменную config
config: ConfigEnv = load_config()
bot = limited_aiogram.LimitedBot(token=config.tg_bot.token)



async def main():
    # await start_http_server()
    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')


    dp = Dispatcher(bot=bot)

    dp.include_router(chat_hendlers.router)
    dp.include_router(handlers.router)

    
    
    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)



if __name__ == '__main__':
    asyncio.run(main())