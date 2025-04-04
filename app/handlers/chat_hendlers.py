import asyncio
import logging
import random

from aiogram import Router, F, Bot
from aiogram.enums import MessageEntityType
from aiogram.fsm.storage.redis import Redis
from aiogram.types import Message, ChatPermissions

from config_data.config import ConfigEnv, load_config

from app.lexicon.lexicon import censorship_list
from app.middleware.album_middleware import AlbumMiddleware

from app.service.functions import validate_text, validate_links

router = Router()
config: ConfigEnv = load_config()

redis = Redis(host=config.redis.host, port=config.redis.port, password=config.redis.password)


ADMIN_IDS = config.tg_bot.admin_ids
CHAT = config.tg_bot.chat_id

router.message.middleware(AlbumMiddleware(0.5, ADMIN_IDS))

logger = logging.getLogger(__name__)

MUTE_DURATION = 86400  # 24 часа в секундах


keywords_realtor = ['#сдам', 'сдам', '#продам', 'продам', 'сдаю', 'сдается']
keywords_client = ['#сниму', 'сниму', 'снять', 'ищу', 'арендую', 'хочу']


@router.message(F.media_group_id)
async def accept_photos(message: Message, bot: Bot, album: list = None):
    user_id = message.from_user.id
    chat_id = message.chat.id
    user_name = message.from_user.username

    message_ids_all = [msg.message_id for msg in album]

    logger.info(f'Пришла медиагруппа от пользователя {user_id}:{user_name}')


    if user_id in ADMIN_IDS:
        return

    text = [msg.caption for msg in album if msg.caption is not None]
    text = text[0].lower().strip()


    if validate_text(text=text, censorship_list=censorship_list):
        """Проверка на мат"""
        logger.info(f'Пользователь не прошел проверку на мат {user_id}:{user_name}')
        await bot.delete_messages(chat_id=chat_id, message_ids=message_ids_all)
        text_error = 'Текст содержит ненормативную лексику!'
        await handle_violation(message, user_name, user_id, text_error)
        return

    if validate_text(text=text, censorship_list=keywords_client):
        logger.info(f'Пропускает допустимые слова и пользователь размещает {user_id}:{user_name}')
        return

    # if config.subscription.subscript:
    #     if not await DataBase.check_user_exists(user_id):
    #         """Проверка в БД"""
    #         await bot.delete_messages(chat_id=chat_id, message_ids=message_ids_all)
    #         await user_no_subscription(message, user_name, user_id)
    #         logger.info(f'Пользователь не прошел проверку БД {user_id}:{user_name}')
    #         return
    #     if not await DataBase.get_subscription_status(user_id):
    #         """Проверка статуса тарифа"""
    #         await bot.delete_messages(chat_id=chat_id, message_ids=message_ids_all)
    #         await user_no_subscription(message, user_name, user_id)
    #         logger.info(f'Пользователь не прошел проверку тарифного плана {user_id}:{user_name}')
    #         return

    if len(album) > 6:
        """Удаляет лишние фото"""
        message_ids_not_caption = [msg.message_id for msg in album if msg.caption is None]
        await bot.delete_messages(chat_id=chat_id, message_ids=message_ids_not_caption[5:])
        logger.info(f'Удалил лишние фото {user_id}:{user_name}')

    if len(text) > 600:
        """Проверка длинны шрифта"""

        await bot.delete_messages(chat_id=chat_id, message_ids=message_ids_all)
        text_error = 'Текст превышает 1500 символов.'
        await handle_violation(message, user_name, user_id, text_error)
        logger.info(f'Пользователь не прошел проверку на количество символов {user_id}:{user_name}')
        return

    if message.entities or message.caption_entities:
        if await check_for_url(message):
            """Проверка на ссылки"""
            text_error = 'Запрещено указывать ссылки на сторонние группы / сайты.'
            await message.delete()
            await handle_violation(message, user_name, user_id, text_error)
            logger.info(f'Пользователь не прошел проверку на ссылки в тексте {user_id}:{user_name}\n{message}')
            return

    if validate_links(text):
        """Проверка на ссылки"""

        await bot.delete_messages(chat_id=chat_id, message_ids=message_ids_all)
        text_error = 'Запрещено указывать ссылки на сторонние группы / сайты.'
        await handle_violation(message, user_name, user_id, text_error)
        logger.info(f'Пользователь не прошел проверку на ссылки в тексте {user_id}:{user_name}')
        return






@router.message(F.new_chat_members)
async def new_members(message: Message):
    pass

@router.message(F.chat.id == int(CHAT))
async def update_revizor(message: Message, bot: Bot):
    user_id = message.from_user.id
    chat_id = message.chat.id
    user_name = message.from_user.username
    # Получение текста сообщения и подписи
    text = (message.text or "") + (message.caption or "")
    text = text.lower().strip()
    message_ids = [message.message_id]

    if user_id in ADMIN_IDS:
        return

    text_error = ''
    await message.delete()
    await handle_violation(message, user_name, user_id, text_error)
    logger.info(f'Проверка пустого сообщения {user_id}:{user_name}')
    return

    # if validate_text(text=text, censorship_list=censorship_list):
    #     """Проверка на мат"""
    #     text_error = 'Текст содержит ненормативную лексику!'
    #     await message.delete()
    #     await handle_violation(message, user_name, user_id, text_error)
    #     logger.info(f'Пользователь не прошел проверку на мат {user_id}:{user_name}')
    #     return
    #
    # if validate_text(text=text, censorship_list=keywords_client):
    #     logger.info(f'Пропускает допустимые слова {user_id}:{user_name}')
    #     """Проверка на сниму"""
    #     return
    # # if config.subscription.subscript:
    # #     if not await DataBase.check_user_exists(user_id):
    # #         """Проверка на наличие в БД"""
    # #         await message.delete()
    # #         await user_no_subscription(message, user_name, user_id)
    # #         logger.info(f'Пользователь не прошел проверку на БД {user_id}:{user_name}')
    # #         return
    # #
    # #     if not await DataBase.get_subscription_status(user_id):
    # #         """Проверка статуса тарифа"""
    # #         await message.delete()
    # #         await user_no_subscription(message, user_name, user_id)
    # #         logger.info(f'Пользователь не прошел проверку на тариф {user_id}:{user_name}')
    # #         return
    # if len(text) == 0:
    #     """Проверка пустого сообщения"""
    #     text_error = ''
    #     await message.delete()
    #     await handle_violation(message, user_name, user_id, text_error)
    #     logger.info(f'Проверка пустого сообщения {user_id}:{user_name}')
    #     return
    # if len(text) > 600:
    #     """Проверка длинны шрифта"""
    #     text_error = 'Текст превышает 600 символов.'
    #     await message.delete()
    #     await handle_violation(message, user_name, user_id, text_error)
    #     logger.info(f'Пользователь не прошел проверку на количество символов {user_id}:{user_name}')
    #     return
    # if message.entities or message.caption_entities:
    #     if await check_for_url(message):
    #         """Проверка на ссылки"""
    #         text_error = 'Запрещено указывать ссылки на сторонние группы / сайты.'
    #         await message.delete()
    #         await handle_violation(message, user_name, user_id, text_error)
    #         logger.info(f'Пользователь не прошел проверку на ссылки в тексте {user_id}:{user_name}')
    #         return
    # if validate_links(text):
    #     """Проверка на ссылки"""
    #     text_error = 'Запрещено указывать ссылки на сторонние группы / сайты.'
    #     await message.delete()
    #     await handle_violation(message, user_name, user_id, text_error)
    #     logger.info(f'Пользователь не прошел проверку на ссылки в тексте {user_id}:{user_name}')
    #     return


async def check_for_url(message: Message):
    # Проверяем наличие сущностей в сообщении
    if message.entities:
        # Перебираем все сущности и проверяем на наличие типа URL
        for entity in message.entities:
            if entity.type in {MessageEntityType.URL, MessageEntityType.TEXT_LINK}:
                return True  # URL найден
    return False  # URL не найден






async def handle_violation(message: Message, user_name: str, user_id: int, text_error: str):
    violation_text = (f'@{user_name}\n<i>{text_error}</i>\nСообщение нарушает <a href="https://t.me/tbilisi_rentflat/154934">правила чата</a>!\n'
                      f'По всем вопросам к <a href="https://t.me/realtyBatumiN1">администратору группы</a>')

    key = f'violation:{user_id}:{violation_text}'
    is_violation = await redis.get(key)
    if not is_violation:
        await asyncio.sleep(random.randint(1, 4))
        warning_message = await message.answer(text=violation_text, disable_notification=True, parse_mode='html', disable_web_page_preview=True)
        await redis.set(key, '1', ex=19)
        await asyncio.sleep(20)
        await warning_message.delete()





