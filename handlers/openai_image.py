from aiogram import Router
from aiogram import F
from aiogram import flags
from states import Gen

from aiogram.utils.chat_action import ChatActionMiddleware
from aiogram.fsm.context import FSMContext

from kb import *
from text import *
from secondary_functions.ai_text import *

router = Router()
router.message.middleware(ChatActionMiddleware())


@router.callback_query(F.data == "gen_image_inline")
async def input_openai_image_promt_callback(callback: types.Message, state: FSMContext):
    await callback.message.answer("Задайте запрос для генерации картинки ")
    await state.set_state(Gen.openai_image)


@router.message(F.text == "Генерация картинки по запросу")
async def input_openai_image_promt(message: types.Message, state: FSMContext):
    await message.answer("Задайте запрос для генерации картинки ")
    await state.set_state(Gen.openai_image)


@router.message(Gen.openai_image)
@flags.chat_action("typing")
async def openai_vopros(message: types.Message, state: FSMContext):
    await message.answer("генерирую картинку, ожидайте...")
    await message.answer(f"{generate_image(message.text)}")
    await message.answer(gen_exit, reply_markup=main_keyboard)
