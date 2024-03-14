from aiogram import Router
from aiogram import F
from aiogram.types import URLInputFile

from kb import *
from text import *


router = Router()


@router.message(F.text == "brat_bake")
async def cmd_random(message: types.Message):
    image_from_url = URLInputFile("https://s3.eu-central-1.amazonaws.com/img.hromadske.ua/posts/282692/1130110jpg/large.jpg")
    result = await message.answer_photo(
        image_from_url,
        caption=brat_bake_description,
        reply_markup=exit_kb
    )


@router.callback_query(F.data == "brat_bake_inline")
async def brat_bake_inline(callback: types.Message):

    image_from_url = URLInputFile("https://s3.eu-central-1.amazonaws.com/img.hromadske.ua/posts/282692/1130110jpg/large.jpg")
    result = await callback.message.answer_photo(
        image_from_url,
        caption=brat_bake_description,
        reply_markup=exit_kb
    )
