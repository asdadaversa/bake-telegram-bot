from aiogram import Router
from aiogram import F
from pydantic import ValidationError
from states import Gen
from aiogram import flags
from aiogram.fsm.context import FSMContext

from secondary_functions.kurs import *
from kb import *
from text import *

router = Router()


@router.message(F.text == "obmenka")
async def obmenka_func(message: types.Message):
    await message.answer(f"{valuta_greet_msg}", reply_markup=obmenka_keyboard)


@router.message(F.text == "USD")
async def usd_msg(message: types.Message):
    await message.reply(kurs_function("USD"))


@router.message(F.text == "AUD")
async def aud_msg(message: types.Message):
    await message.reply(kurs_function("AUD"))


@router.message(F.text == "EUR")
async def eur_msg(message: types.Message):
    await message.reply(kurs_function("EUR"))


@router.message(F.text == "SEK")
async def sec_func(message: types.Message):
    await message.reply(kurs_function("SEK"))


@router.message(F.text == "GBP")
async def gbp_func(message: types.Message):
    await message.reply(kurs_function("GBP"))


@router.message(F.text == "PLN")
async def pln_func(message: types.Message):
    await message.reply(kurs_function("PLN"))


@router.message(F.text == "Другая валюта")
async def other_currency_func(message: types.Message, state: FSMContext):
    await message.answer(f"{valuta_msg}",)
    await state.set_state(Gen.obmenka)


@router.message(Gen.obmenka)
@flags.chat_action("typing")
async def answer(message: types.Message):
    try:
        await message.reply(kurs_function(f"{message.text}"))
    except ValidationError:
        await message.reply(f"{valuta_error_msg}")

    await message.answer(f"{valuta_msg}", reply_markup=obmenka_keyboard)


@router.callback_query(F.data == "obmenka_inline")
async def callback_obmenka(callback: types.CallbackQuery):

    await callback.message.answer(f"{valuta_greet_msg}", reply_markup=obmenka_keyboard)
