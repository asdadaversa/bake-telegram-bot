from aiogram import Router
from aiogram import F
from secondary_functions.pogoda import *
from kb import *
from text import *
from aiogram.fsm.context import FSMContext
from states import Gen
from aiogram.fsm.context import FSMContext
from states import Gen
from aiogram import flags

router = Router()


@router.message(F.text == "pogoda")
async def pogoda(message: types.Message):
    await message.answer(f"{pogoda_msg}", reply_markup=keyboard_pogoda)


@router.message(F.text == "Киев")
async def pogoda_kiev(message: types.Message):
    await message.reply(pogoda_function("Kiev"))


@router.message(F.text == "Львов")
async def pogoda_lviv(message: types.Message):
    await message.reply(pogoda_function("Lviv"))


@router.message(F.text == "Париж")
async def pogoda_paris(message: types.Message):
    await message.reply(pogoda_function("Paris"))


@router.message(F.text == "Рим")
async def pogoda_rome(message: types.Message):
    await message.reply(pogoda_function("Rome"))


@router.message(F.text == "Барселона")
async def pogoda_barcelona(message: types.Message):
    await message.reply(pogoda_function("Barselona"))

# @router.message(F.text == "Другая валюта")
# async def other_currency_func(message: types.Message, state: FSMContext):
#     await message.answer(f"{valuta_msg}",)
#     await state.set_state(Gen.obmenka)
#
#
# @router.message(Gen.obmenka)
# @flags.chat_action("typing")
# async def answer(message: types.Message):
#     try:
#         await message.reply(kurs_function(f"{message.text}"))
#     except ValidationError:
#         await message.reply(f"{valuta_error_msg}")
#
#     await message.answer(f"{valuta_msg}", reply_markup=obmenka_keyboard)


@router.message(F.text == "Другой город")
async def pogoda_other(message: types.Message, state: FSMContext):
    await message.answer(f"{pogoda_other_msg}")
    await state.set_state(Gen.pogoda)


@router.message(Gen.pogoda)
@flags.chat_action("typing")
async def answer(message: types.Message):
    try:
        await message.reply(pogoda_function(f"{message.text}"))
    except KeyError:
        await message.reply(f"{message.text}?🤣 вы серьезно?🤣 такого города, к сожалению, не существует\n")

    await message.answer(f"{pogoda_other_msg}", reply_markup=keyboard_pogoda)


@router.callback_query(F.data == "pogoda_inline")
async def pogoda_inline(callback: types.Message):

    await callback.message.answer(f"{pogoda_msg}", reply_markup=keyboard_pogoda)

