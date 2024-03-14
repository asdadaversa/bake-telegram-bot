from aiogram import Router
from kb import *

router = Router()


@router.message()
async def answer(message: types.Message):
    await message.answer("Это бот - для связи с администратрацией  напишите на brat_bake@gmail.com")
