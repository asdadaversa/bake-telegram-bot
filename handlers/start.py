from aiogram import Router, Bot
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext

from kb import *

bot = Bot(token="6239139377:AAG9MphHAmTK83tWqMdtqh8qO6ujKiafjVw")
router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message, state: FSMContext):
    await state.clear()
    info = await bot.get_me()
    name = info.username

    await message.answer(
        f"Добрый вечерочек, {message.from_user.first_name}, "
        f"тебя приветствует бот - {name.upper()}, ниже меню",
        reply_markup=start_keyboard
    )
