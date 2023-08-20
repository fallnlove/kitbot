import asyncio
import aiogram
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from kitbot.utils import config
from kitbot.utils import load_handlers


async def main() -> None:
    bot = aiogram.Bot(token=config.token)
    try:
        storagegit = MemoryStorage()
        disp = aiogram.Dispatcher(bot=bot, storage=storage)

        await load_handlers.main(disp)

        await disp.start_polling()
    except Exception as error:
        await bot.close_bot()
        print(error)

if __name__ == '__main__':
    asyncio.run(main())
