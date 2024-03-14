import asyncio
from aiogram import Bot, Dispatcher

from handlers import (
    obmenka,
    menu,
    pogoda,
    lukashenko,
    start,
    bake,
    avtootvet,
    brat_bake,
    crypta,
    openai_vopros,
    openai_image
)


async def main():
    bot = Bot(token="6239139377:AAG9MphHAmTK83tWqMdtqh8qO6ujKiafjVw")
    dp = Dispatcher()

    dp.include_router(start.router)
    dp.include_router(menu.router)
    dp.include_router(openai_image.router)
    dp.include_router(openai_vopros.router)
    dp.include_router(obmenka.router)
    dp.include_router(pogoda.router)
    dp.include_router(crypta.router)
    dp.include_router(lukashenko.router)
    dp.include_router(bake.router)
    dp.include_router(brat_bake.router)
    dp.include_router(avtootvet.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
