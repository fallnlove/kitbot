import os
import aiogram
import asyncio

from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from ..create_award import create
from PIL import Image


async def make_file(event: aiogram.types.Message, state: FSMContext) -> None:
    await state.finish()
    user_name = event.text
    file_name = await create.main(user_name, event.from_user.id)
    await event.reply_document(open(file_name, 'rb'))
    await event.reply("Если вы обшились в написании ФИО, то перейдите по ссылке еще раз")

    os.remove(file_name)
