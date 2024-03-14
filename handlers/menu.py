from aiogram import Router
from aiogram import F
from aiogram.fsm.context import FSMContext

from kb import *


router = Router()


@router.message(F.text == "Меню")
async def menu(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "Главное меню",
        reply_markup=main_menu
    )


@router.callback_query(F.data == "menu")
async def menu(callback: types.CallbackQuery):
    await callback.message.answer(
        "выходим в главное меню",
        reply_markup=main_menu
    )
