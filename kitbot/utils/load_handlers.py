import aiogram

from ..commands import start, make_file
from ..utils import message_states


async def main(disp: aiogram.Dispatcher) -> None:
    disp.register_message_handler(start.start_message, commands={"start", "restart", "help"})

    disp.register_message_handler(make_file.make_file, state=message_states.MessageStates.AskUsername)
