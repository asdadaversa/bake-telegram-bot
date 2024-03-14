from aiogram import Router
from aiogram import F
from states import Gen
from aiogram import flags
from aiogram.fsm.context import FSMContext

from kb import *
from secondary_functions.crypta import *
from text import *

router = Router()

    
@router.message(F.text == "crypta")
async def crypta(message: types.Message):
    await message.answer(f"{crypta_msg}", reply_markup=keyboard_crypta)


@router.message(F.text == "BTC")
async def aud_func(message: types.Message):
    await message.reply(crypto_price("BTC"))


@router.message(F.text == "ETH")
async def aud_func(message: types.Message):
    await message.reply(crypto_price("ETH"))


@router.message(F.text == "SOL")
async def sol_func(message: types.Message):
    await message.reply(crypto_price("SOL"))


@router.message(F.text == "XRP")
async def aud_func(message: types.Message):
    await message.reply(crypto_price("XRP"))


@router.message(F.text == "ADA")
async def aud_func(message: types.Message):
    await message.reply(crypto_price("ADA"))


@router.message(F.text == "DOGE")
async def aud_func(message: types.Message):
    await message.reply(crypto_price("DOGE"))


@router.message(F.text == "SHIB")
async def aud_func(message: types.Message):
    await message.reply(crypto_price("SHIB"))


@router.message(F.text == "Другая монета")
async def other_coin_funct(message: types.Message, state: FSMContext):
    await message.answer("введите название монеты (к примеру BTC)")
    await state.set_state(Gen.crypta)


@router.message(Gen.crypta)
@flags.chat_action("typing")
async def answer(message: types.Message, state: FSMContext):
    await message.reply(f"{crypto_price(message.text)}")

    await message.answer(
        "введите название монеты (к примеру BTC)",
        reply_markup=keyboard_crypta
    )


@router.callback_query(F.data == "crypta_inline")
async def crypta(callback: types.Message):

    await callback.message.answer(f"{crypta_msg}", reply_markup=keyboard_crypta)


