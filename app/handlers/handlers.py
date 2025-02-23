import logging
import asyncio
from aiogram import types, Router, Bot, F
from aiogram.filters import Command, CommandStart

router = Router()

logger = logging.getLogger(__name__)


@router.message(CommandStart())
async def command_start_handler(message: types.Message):

    await message.answer(text=f'<a href="https://t.me/tbilisi_rentflat/154934">правила чата</a>!\n'
                      f'По всем вопросам к <a href="https://t.me/realtyBatumiN1">администратору группы</a>')
