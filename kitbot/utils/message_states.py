from aiogram.dispatcher.filters.state import State, StatesGroup


class MessageStates(StatesGroup):
    AskUsername = State()
