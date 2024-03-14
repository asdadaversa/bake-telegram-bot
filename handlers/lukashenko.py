from aiogram import Router
from aiogram import F
from aiogram.types import FSInputFile, URLInputFile

from kb import *

router = Router()


@router.message(F.text == "lukashenko")
async def cmd_random(message: types.Message):
    image_from_url = URLInputFile("https://gdb.rferl.org/08610000-0a00-0242-845e-08d9fbb2f7e9_cx9_cy0_cw82_w1023_r1_s.jpg")
    await message.answer_photo(
        image_from_url,
        caption="Нажмите на кнопку, чтобы Лукашенко показал 4 позиции"
    )

    await message.answer(
        "а я вам покажу...",
        reply_markup=lukasheno_keyboard
    )


@router.callback_query(F.data == "lukashenko_kartinka")
async def send_4_pozicii(callback: types.CallbackQuery):
    image_from_pc = FSInputFile("4pozicii.png")
    result = await callback.message.answer_photo(
        image_from_pc,
        caption="4 позиции, откуда на Беларусь готовилось нападение..."
    )


@router.callback_query(F.data == "lukashenko_ssulka")
async def send_4_pozicii(callback: types.CallbackQuery):
    await callback.message.answer("https://www.google.com/maps/search//@52.2617658,27.8609158,7z/data=!4m19!1m15!4m14!1m6!1m2!1s0x40d4cf4ee15a4505:0x764931d2170146fe!2z0LrQuNC10LI!2m2!1d30.5245025!2d50.4503596!1m6!1m2!1s0x46dbcfd35b1e6ad3:0xb61b853ddb570d9!2z0LzQuNC90YHQug!2m2!1d27.558972!2d53.9006011!2m2!3m1!5e2?entry=ttu")


@router.callback_query(F.data == "lukashenko_inline")
async def lukashenko_inline(callback: types.CallbackQuery):
    image_from_url = URLInputFile("https://gdb.rferl.org/08610000-0a00-0242-845e-08d9fbb2f7e9_cx9_cy0_cw82_w1023_r1_s.jpg")
    await callback.message.answer_photo(
        image_from_url,
        caption="Нажмите на кнопку, чтобы Лукашенко показал 4 позиции"
    )
    await callback.message.answer(
        "а я вам покажу...",
        reply_markup=lukasheno_keyboard
    )
