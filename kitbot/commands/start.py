import aiogram
import asyncio

from aiogram.dispatcher import FSMContext
from ..utils import message_states


async def start_message(event: aiogram.types.Message, state: FSMContext) -> None:
    await event.answer(f"""Чтобы получить диплом олимпиады, отправьте свое ФИО""")
    await state.set_state(message_states.MessageStates.AskUsername)
