from aiogram import Router
from aiogram import F
from aiogram.types import URLInputFile

from kb import *
from text import *


router = Router()


@router.message(F.text == "bake")
async def cmd_random(message: types.Message):

    image_from_url = URLInputFile("https://www.meme-arsenal.com/memes/6754336880c26b3517d8bfe716409d37.jpg")
    await message.answer_photo(
        image_from_url,
        caption=bake_description,
        reply_markup=exit_kb
    )


@router.callback_query(F.data == "bake_inline")
async def bake_inline(callback: types.Message):
    image_from_url = URLInputFile("https://www.meme-arsenal.com/memes/6754336880c26b3517d8bfe716409d37.jpg")
    await callback.message.answer_photo(
        image_from_url,
        caption=bake_description,
        reply_markup=main_keyboard
    )
